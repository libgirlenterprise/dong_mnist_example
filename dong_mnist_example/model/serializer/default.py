import tensorflow


def write(self, save_dir):

    export_path = save_dir + 'my_model.h5'
    self.save(export_path)

def read(self, save_dir):
    
    model = tensorflow.keras.models.load_model(save_dir + 'my_model.h5',
                                               custom_objects={
                                                   'DefaultModel': tensorflow.keras.models.Sequential
                                               })
    self.set_weights(model.get_weights())
