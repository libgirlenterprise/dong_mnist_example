

import json

import tabemasu.data
import tabemasu.models.mlp
import tabemasu.train


def main():
    with open('tabemasu/train.json') as f:
        model, score = tabemasu.train.train(model=tabemasu.models.mlp.new(tabemasu.data.get_data_params()),
                                            train_data=tabemasu.data.get_train_data(),
                                            eval_data=tabemasu.data.get_eval_data(),
                                            config=json.load(f))
        print(score)
