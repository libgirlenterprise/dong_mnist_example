from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json, numpy
import dong.framework
from dong_mnist_example.model.init.default_load import DefaultModelLoad
from dong_mnist_example.data.default import DefaultData

class DefaultService(DefaultModelLoad, dong.framework.Service):

    def __init__(self, save_dir):
        data = DefaultData()
        super().__init__(data_params=data.get_data_params(),
                         save_dir=save_dir)
    
    def on_request(self, request_body, mime_type='application/json'): 

        data = json.loads(request_body)
        x = numpy.array(data) / 255.0
        return json.dumps(self.predict(x).tolist())
