
def name():
    return 'TRAIN_SCRIPT_NAME'

def train(model, train_data, eval_data=None, config={}):

    train_config_from_file = configparser.ConfigParser()
    train_config_from_file.read( name() + '.ini')
    train_config = {**train_config_from_file, **config}
    
    # Editor below to write your training code
    # Finally, return the training scores
    
    scores = 1.0
    return scores
