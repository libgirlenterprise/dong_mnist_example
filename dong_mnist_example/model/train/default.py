


def train(self, data, config=None):

    more_args_dict = {
        'self.fit': [data.get_train_data().x, data.get_train_data().y]
    }

    self.run_ordered_dict_as_procedure(config, more_args_dict)
    
    return self.evaluate(data.get_eval_data().x,
                         data.get_eval_data().y)[1]
