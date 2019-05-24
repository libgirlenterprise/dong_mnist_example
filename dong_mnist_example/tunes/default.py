from dong_mnist_example.tunes import HyperParameterSequence

def get_hyper_parameter_collection():

    config_template =  {
        "optimizer": "adam",
        "loss": "sparse_categorical_crossentropy",
        "metrics": [ "accuracy" ]
    }
    hyper_parameter_list = []
    for i in [1, 3, 5]:
        hyper_parameter_dict = {}
        hyper_parameter_dict['compile'] = config_template
        hyper_parameter_dict['fit'] = { 'epochs' : i }
        hyper_parameter_list.append(HyperParameterSequence(hyper_parameter_dict, None))

    return hyper_parameter_list

def get_best_model_score_pair(model_score_pair_collection):

    def get_score(model_score_pair):
        return model_score_pair.score

    return max(model_score_pair_collection, key=get_score)
        
