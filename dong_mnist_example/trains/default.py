from dong_mnist_example.trains import ModelScorePair

def train(model, train_data, eval_data=None, config={}):

    model.compile(**config['compile'])    
    model.fit(train_data.x, train_data.y, epochs=config['fit']['epochs'])
    
    return ModelScorePair(model, model.evaluate(eval_data.x, eval_data.y)[1])
