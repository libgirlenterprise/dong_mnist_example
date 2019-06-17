from dong.framework import HyperParameterConfig, HyperParameterTuner
from dong_mnist_example.config.default import get_config
import copy

class DefaultTune(HyperParameterTuner):

    def get_hyper_parameter_config_list(self):
        config = get_config()

        config_list = []

        for i in [1, 3, 5]:
            hyper_parameter_ordered_dict = copy.deepcopy(config)
            hyper_parameter_ordered_dict['self.fit'] = ( ':epochs' , i )
            config_list.append(HyperParameterConfig(hyper_parameter_ordered_dict, None))

        return config_list

    
