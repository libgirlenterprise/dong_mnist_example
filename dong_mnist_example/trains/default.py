

def train(model, train_data, eval_data=None, config={}):

    model.compile(**config['compile'])    
    model.fit(train_data.x, train_data.y, epochs=config['fit']['epochs'])
    
    return model, model.evaluate(eval_data.x, eval_data.y)[1]
