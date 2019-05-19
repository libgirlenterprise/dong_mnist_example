import tensorflow

def save(model, save_dir):
    model.save(save_dir + 'my_model.h5')
    pass

def load(save_dir):
    return tensorflow.keras.models.load_model( save_dir + 'my_model.h5')
    
    
