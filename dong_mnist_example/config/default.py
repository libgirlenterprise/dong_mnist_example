from collections import OrderedDict

def get_config():
    return OrderedDict([("self.compile", (":optimizer",
                                          "adam",
                                          ":loss",
                                          "sparse_categorical_crossentropy",
                                          ":metrics",
                                          [ "accuracy" ])),
                        ("self.fit", (":epochs", 5))])
