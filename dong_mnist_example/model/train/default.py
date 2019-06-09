
def train(self, data, config=None):

    order_dict_as_procedure(config)
    
    return self.evaluate(data.get_eval_data().x,
                         data.get_eval_data().y)[1]
