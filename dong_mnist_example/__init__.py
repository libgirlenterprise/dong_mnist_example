
import argparse
import sys
import json
import os
import pkgutil
import importlib

def main():
    project_name = sys.argv[0].split('/')[-1]
    args = sys.argv[1:]
    parser = argparse.ArgumentParser()

    parser.add_argument('--data-module', action='store', type=str, default='default')
    parser.add_argument('--data-class', action='store', type=str, default='DefaultData')
    parser.add_argument('--model-module', action='store', type=str, default='default')
    parser.add_argument('--model-class', action='store', type=str, default='DefaultTrainModel')
    parser.add_argument('--tune-module', action='store', type=str, default='default')
    parser.add_argument('--tune-class', action='store', type=str, default='DefaultTune')

    parser.add_argument('--do-tune', action='store_true')
    
    parser.add_argument('--train-config-module', action='store', type=str)
    parser.add_argument('--train-config-func', action='store', type=str)
    
    args, _ = parser.parse_known_args(args)

    
    model_module = importlib.import_module(project_name + '.model.' + args.model_module)
    data_module = importlib.import_module(project_name + '.data.' + args.data_module)
    Data = getattr(data_module,
                   args.data_class)
    Model = getattr(model_module, args.model_class)

    if args.do_tune:
        tune_module = importlib.import_module(project_name + '.tune.' + args.tune_module)
        Tune = getattr(tune_module, args.tune_class)
        tune = Tune()
        model_score_pair_list = []
        config_list = tune.get_hyper_parameter_config_list()

        for hyper_parameter_config in config_list:
            data = Data(config=hyper_parameter_config.get_config())

            model = Model(data_params=data.get_data_params(),
                          config=hyper_parameter_config.get_config())
            score = model.train(data=data,
                                config=hyper_parameter_config.get_config())
            model_score_pair_list.append((model, score))

        def get_sec(tup):
            return tup[1]
        
        model_score_pair = max(model_score_pair_list, key=get_sec)
        (model, score) = model_score_pair
        
    else:
        train_config = None

        if args.train_config_module is not None and args.train_config_func is not None:
            train_config_module = importlib.import_module(project_name + '.model.train.' + args.train_config_module)
            train_config = getattr(train_config_module, args.train_config_func)()

            data = Data(config=train_config)

            model = Model(data_params=data.get_data_params(),
                          config=train_config)
            score = model.train(data=data,
                                config=train_config)
        
    os.makedirs(os.environ.get('MODEL_SAVE_DIR'), exist_ok=True)
    model.write(os.environ.get('MODEL_SAVE_DIR') + '/')
    print('Evaluation Accuracy: ' + str(score))
