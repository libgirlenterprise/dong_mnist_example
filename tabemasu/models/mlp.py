hidden_units=512
dropout=0.2

def new(data_params=None):
    return tensorflow.keras.models.Sequential([
        tensorflow.keras.layers.Flatten(input_shape=(data_params.image_size, data_params.image_size)),
        tensorflow.keras.layers.Dense(hidden_units, activation=tensorflow.nn.relu),
        tensorflow.keras.layers.Dropout(dropout),
        tensorflow.keras.layers.Dense(data_params.num_labels, activation=tensorflow.nn.softmax)
    ])

