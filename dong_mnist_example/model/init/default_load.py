import tensorflow
from dong_mnist_example.model.init.default import DefaultModelInit
from dong_mnist_example.data.default import DefaultData

class DefaultModelLoad(DefaultModelInit):

    def __init__(self, config={}, save_dir=None):

        data = DefaultData()
        super().__init__(config,
                         data_params=data.get_data_params(),
                         save_dir=save_dir)
        model = tensorflow.keras.models.load_model(save_dir + 'my_model.h5',
                                                   custom_objects={
                                                       'DefaultTrainModel': tensorflow.keras.models.Sequential
                                                   })
        self.set_weights(model.get_weights())


