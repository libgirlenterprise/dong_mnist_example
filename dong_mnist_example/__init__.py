
import argparse
import sys
import json
import os
import pkgutil
import importlib
from dong.framework import HyperParameterConfig

def main():
    project_name = sys.argv[0].split('/')[-1]
    args = sys.argv[1:]
    parser = argparse.ArgumentParser()

    parser.add_argument('--data-module', action='store', type=str, default='default')
    parser.add_argument('--data-class', action='store', type=str)
    parser.add_argument('--model-module', action='store', type=str, default='default')
    parser.add_argument('--model-class', action='store', type=str)
    parser.add_argument('--config-module', action='store', type=str)
    parser.add_argument('--config-func', action='store', type=str, default='get_config')
    parser.add_argument('--do-tune', action='store_true')
    parser.add_argument('--tune-module', action='store', type=str, default='default')
    parser.add_argument('--tune-class', action='store', type=str)

    def get_module_class(module_type_str):
        module_name = getattr(args, module_type_str + '_module')
        module = importlib.import_module(project_name + '.' + module_type_str +'.' + module_name)
        module_class_name =  getattr(args, module_type_str + '_class')
        if module_class_name is None:
            module_class_name = module_name.title() + module_type_str.title()
        return getattr(module, module_class_name)
    
    args, _ = parser.parse_known_args(args)
    
    Data = get_module_class('data')
    Model = get_module_class('model')

    config_list = []
    model_score_pair_list = []
    
    if args.do_tune:
        Tune = get_module_class('tune')
        tune = Tune()
        config_list = tune.get_hyper_parameter_config_list()
    else:
        config = None
        if args.config_module is not None:
            config_module = importlib.import_module(project_name + '.config.' + args.config_module)
            config = getattr(config_module, args.config_func)()
        config_list.append(HyperParameterConfig(config))

    for hyper_parameter_config in config_list:
        data = Data(config=hyper_parameter_config.get_config())
        model = Model(data_params=data.get_data_params(),
                      config=hyper_parameter_config.get_config())
        score = model.train(data=data,
                            config=hyper_parameter_config.get_config())
        model_score_pair_list.append((model, score))
        model_score_pair = max(model_score_pair_list, key=lambda tup: tup[1])
        (model, score) = model_score_pair
        
    os.makedirs(os.environ.get('MODEL_SAVE_DIR'), exist_ok=True)
    model.write(os.environ.get('MODEL_SAVE_DIR') + '/')
    print('Evaluation Accuracy: ' + str(score))
