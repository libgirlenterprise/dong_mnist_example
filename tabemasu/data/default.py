
from __future__ import (absolute_import, division, print_function,
    unicode_literals)

import collections
import numpy
import tensorflow


DataPair = collections.namedtuple('DataPair', ['x', 'y'])
DataParams = collections.namedtuple('Params', ['image_size', 'num_labels'])
                                
mnist = tensorflow.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

image_size = x_train.shape[1]
input_size = image_size * image_size

x_train, x_test = x_train / 255.0, x_test / 255.0
                        
num_labels = len(numpy.unique(y_train))
    

def get_train_data():
    return DataPair(x_train, y_train)

def get_eval_data():
    return DataPair(x_test, y_test)

def get_data_params():
    return DataParams(image_size, num_labels)
