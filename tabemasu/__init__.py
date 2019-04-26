

import json
import os
import tabemasu.data
import tabemasu.models.mlp
import tabemasu.save_load
import tabemasu.train


def main():
    with open('tabemasu/train.json') as f:
        model, score = tabemasu.train.train(model=tabemasu.models.mlp.new(tabemasu.data.get_data_params()),
                                            train_data=tabemasu.data.get_train_data(),
                                            eval_data=tabemasu.data.get_eval_data(),
                                            config=json.load(f))
        os.makedirs("/tmp/save_dir", exist_ok=True)
        tabemasu.save_load.save(model, '/tmp/save_dir/')
        print(score)
