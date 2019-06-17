# dong_mnist_example : a dong train exec sample project
## Installation
Under the project folder
```sh
$ pip install .
```

## Usage
### Training Output Location
- Environment variable ```MODEL_SAVE_DIR``` will be the training output directory
### Command
```shell
USAGE: dong_mnist_example [OPTIONS]

OPTIONS:

    --data-module TEXT
    --data-class TEXT
    --model-module TEXT
    --model-class TEXT
    --train-config-module TEXT
    --train-config-func TEXT
    
    --do-tune: flag for applying hyperparameter tuning or not
    --tune-module TEXT
    --tune-class TEXT

```
### Sample Command
#### Train
```shell
$ dong_mnist_example --train-config-module default_config --train-config-func get_train_config 
```
Which uses default modules.
And here is the equivalent command
```shell
$ dong_mnist_example --data-module default --data-class DefaultData --model-module default --model-class DefaultTrainModel --train-config-module default_config --train-config-func get_train_config 
```
#### Tune
```shell
$ dong_mnist_example --do-tune
```
Which uses default modules.
And here is the equivalent command
```shell
$ dong_mnist_example --do-tune --data-module default --data-class DefaultData --model-module default --model-class DefaultTrainModel
```
