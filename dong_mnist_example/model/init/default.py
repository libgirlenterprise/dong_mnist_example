import tensorflow

# a model collection can be one model with potential to become other models
class DefaultModelInit(tensorflow.keras.models.Sequential):

    _hidden_units=512
    _dropout=0.2

    def __init__(self, config={}, data_params=None, save_dir=None):
        super().__init__([
            tensorflow.keras.layers.Flatten(input_shape=(data_params.image_size, data_params.image_size)),
            tensorflow.keras.layers.Dense(self._hidden_units, activation=tensorflow.nn.relu),
            tensorflow.keras.layers.Dropout(self._dropout),
            tensorflow.keras.layers.Dense(data_params.num_labels, activation=tensorflow.nn.softmax)
        ])
