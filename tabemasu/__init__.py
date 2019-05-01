
import argparse
import sys
import json
import os
import tabemasu.data
import tabemasu.models.mlp
import tabemasu.save_load
import tabemasu.train
import tabemasu.endpoint
import pkgutil

def main():
    
    args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_predict', default=False, action='store_true')
    args, _ = parser.parse_known_args(args)

    if args.test_predict:
        print(tabemasu.endpoint.respond_to_request(model=tabemasu.save_load.load(os.environ.get('MODEL_SAVE_DIR')),
                                                   request_body_json=json.dumps(tabemasu.data.get_eval_data().x[3:5].tolist())))
    else:
        model, score = tabemasu.train.train(model=tabemasu.models.mlp.new(tabemasu.data.get_data_params()),
                                            train_data=tabemasu.data.get_train_data(),
                                            eval_data=tabemasu.data.get_eval_data(),
                                            config=json.loads(pkgutil.get_data('tabemasu', 'train.json')))
        os.makedirs(os.environ.get('MODEL_SAVE_DIR'), exist_ok=True)
        tabemasu.save_load.save(model, os.environ.get('MODEL_SAVE_DIR') + '/')
        print(score)
        
