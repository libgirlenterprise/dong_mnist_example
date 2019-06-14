import tensorflow
from dong_mnist_example.model.init.default import DefaultModelInit
from dong_mnist_example.data.default import DefaultData

class DefaultModelLoad(DefaultModelInit):

    from dong_mnist_example.model.serializer.default import read
    
    def __init__(self, config={}, data_params=None, save_dir=None):

        data = DefaultData()
        super().__init__(config,
                         data_params=data.get_data_params(),
                         save_dir=save_dir)
        self.read(save_dir)

