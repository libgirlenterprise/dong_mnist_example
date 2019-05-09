
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

    parser.add_argument('--data-fetch', action='store', type=str)
    parser.add_argument('--model-set', action='store', type=str)
    parser.add_argument('--save-load', action='store', type=str)
    parser.add_argument('--train', action='store', type=str)
    
    args, _ = parser.parse_known_args(args)

    save_load_module = importlib.import_module(project_name + '.save_load.' + args.save_load)
    model_set_module = importlib.import_module(project_name + '.models.' + args.model_set)
    data_fetch_module = importlib.import_module(project_name + '.data.' + args.data_fetch)
    train_module = importlib.import_module(project_name + '.trains.' +  args.train)
    
    model, score = train_module.train(model=model_set_module.new(data_fetch_module.get_data_params()),
                                      train_data=data_fetch_module.get_train_data(),
                                      eval_data=data_fetch_module.get_eval_data(),
                                      config=json.loads(pkgutil.get_data(project_name, 'trains/' + args.train + '.json')))
    os.makedirs(os.environ.get('MODEL_SAVE_DIR'), exist_ok=True)
    save_load_module.save(model, os.environ.get('MODEL_SAVE_DIR') + '/')
    print(score)
    
