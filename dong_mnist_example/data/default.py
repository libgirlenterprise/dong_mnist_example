
from __future__ import division

import collections
import numpy
import tensorflow
import dong.framework

DataPair = collections.namedtuple('DataPair', ['x', 'y'])
DataParams = collections.namedtuple('Params', ['image_size', 'num_labels'])

class DefaultData(dong.framework.Data):

    
    def __init__(self, config=None):
                                
        mnist = tensorflow.keras.datasets.mnist
        (x_train, self._y_train), (x_test, self._y_test) = mnist.load_data()

        self._x_train, self._x_test = x_train / 255.0, x_test / 255.0

    def get_train_data(self):
        return DataPair(self._x_train, self._y_train)

    def get_eval_data(self):
        return DataPair(self._x_test, self._y_test)

    def get_data_params(self):
    
        image_size = self._x_train.shape[1]
        num_labels = len(numpy.unique(self._y_train))
        return DataParams(image_size, num_labels)
