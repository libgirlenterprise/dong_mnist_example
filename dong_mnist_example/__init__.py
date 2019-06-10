
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
    parser.add_argument('--train-config-module', action='store', type=str)
    parser.add_argument('--train-config-func', action='store', type=str)
    
    args, _ = parser.parse_known_args(args)
    model_module = importlib.import_module(project_name + '.model.' + args.model_module)
    data_module = importlib.import_module(project_name + '.data.' + args.data_module)
    train_config = None
    
    if args.train_config_module is not None and args.train_config_func is not None:
        train_config_module = importlib.import_module(project_name + '.model.train.' + args.train_config_module)
        train_config = getattr(train_config_module, args.train_config_func)()

    Data = getattr(data_module, args.data_class)
    data = Data()
    Model = getattr(model_module, args.model_class)
    model = Model(data_params=data.get_data_params())
    score = model.train(data=data,
                        config=train_config)
        
    os.makedirs(os.environ.get('MODEL_SAVE_DIR'), exist_ok=True)
    model.commit(os.environ.get('MODEL_SAVE_DIR') + '/')
    print('Evaluation Accuracy: ' + str(score))
