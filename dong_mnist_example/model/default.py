from dong_mnist_example.model.init.default import DefaultModelInit
import dong.framework

class DefaultModel(DefaultModelInit, dong.framework.Model):

    from dong_mnist_example.model.train.default import train
    from dong_mnist_example.model.serializer.default import write
