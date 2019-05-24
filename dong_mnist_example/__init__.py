
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

    parser.add_argument('--data-fetch', action='store', type=str, default='default')
    parser.add_argument('--model-set', action='store', type=str, default='default')
    parser.add_argument('--save-load', action='store', type=str, default='default')
    parser.add_argument('--train', action='store', type=str, default='default')
    parser.add_argument('--do-tune', action='store_true')
    parser.add_argument('--tune', action='store', type=str, default='default')
    
    
    args, _ = parser.parse_known_args(args)
    save_load_module = importlib.import_module(project_name + '.save_load.' + args.save_load)
    model_set_module = importlib.import_module(project_name + '.models.' + args.model_set)
    data_fetch_module = importlib.import_module(project_name + '.data.' + args.data_fetch)
    train_module = importlib.import_module(project_name + '.trains.' +  args.train)
    model_score_pair = None

    if args.do_tune:
        tune_module = importlib.import_module(project_name + '.tunes.' +  args.tune)
        hyper_parameter_sequence_list = tune_module.get_hyper_parameter_collection()

        model_score_pair_list = []
        for hyper_parameter_sequence in hyper_parameter_sequence_list:
            model_score_pair_list.append(train_module.train(model=model_set_module.new(data_fetch_module.get_data_params()),
                                                            train_data=data_fetch_module.get_train_data(),
                                                            eval_data=data_fetch_module.get_eval_data(),
                                                            config=hyper_parameter_sequence.hyper_parameter_dict))

        model_score_pair = tune_module.get_best_model_score_pair(model_score_pair_list)
        
                                   
    else:
        model_score_pair = train_module.train(model=model_set_module.new(data_fetch_module.get_data_params()),
                                              train_data=data_fetch_module.get_train_data(),
                                              eval_data=data_fetch_module.get_eval_data(),
                                              config=json.loads(pkgutil.get_data(project_name, 'trains/' + args.train + '.json')))
        
    os.makedirs(os.environ.get('MODEL_SAVE_DIR'), exist_ok=True)
    save_load_module.save(model_score_pair.model, os.environ.get('MODEL_SAVE_DIR') + '/')
    print('Evaluation Accuracy: ' + str(model_score_pair.score))
