import tensorflow
from dong_mnist_example.model.init.default import DefaultModelInit


class DefaultModelLoad(DefaultModelInit):

    def __init__(self, config={}, data_params=None, save_dir=None):

        super().__init__(config, data_params, save_dir)
        model = tensorflow.keras.models.load_model(save_dir + 'my_model.h5',
                                                   custom_objects={
                                                       'DefaultTrainModel': tensorflow.keras.models.Sequential
                                                   })
        self.set_weights(model.get_weights())


