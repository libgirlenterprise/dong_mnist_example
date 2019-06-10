from dong_mnist_example.model.init.default import DefaultModelInit
import dong.framework

class DefaultTrainModel(DefaultModelInit, dong.framework.Model):

    from dong_mnist_example.model.train.default import train
    from dong_mnist_example.model.commit.default import commit
