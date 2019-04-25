

def train(model, train_data, eval_data=None, config={}):

    model.compile(**config['compile'])    
    model.fit(x_train, y_train, epochs=config['fit']['epochs'])
    
    return model, model.evaluate(x_test, y_test)[1]
