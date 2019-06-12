from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json, numpy
import dong.framework
from dong_mnist_example.model.init.default_load import DefaultModelLoad


class DefaultService(DefaultModelLoad, dong.framework.Service):

    @dong.framework.request_handler
    def normal(self, request_body, mime_type='application/json'): 

        data = json.loads(request_body)
        x = numpy.array(data) / 255.0
        return json.dumps(self.predict(x).tolist())

    @dong.framework.request_handler
    def hello(self, request_body, mime_type='application/json'): 

        return json.dumps('hello')
