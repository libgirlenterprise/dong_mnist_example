from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json, numpy

def respond_to_request(model, request_body_json): # should support more formats
    data = json.loads(request_body_json)
    x = numpy.array(data) / 255.0
    return json.dumps(model.predict(x).tolist())
