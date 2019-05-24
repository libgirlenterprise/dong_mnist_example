# dong_mnist_example : a dong train/tune exec sample project
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

   --data-fetch: the module handling data fetching

   --model-set: the module indicating a model set
   
   --save-load: the module handling model serialization/deserialization
   
   --train: the module of training program
   
   --do-tune: flag for applying hyperparameter tuning or not
   
   --tune: the module of tuning program
```
### Sample Command
#### Train
```shell
$ dong_mnist_example 
```
Which uses default modules.
And here is the equivalent command
```shell
$ dong_mnist_example --data-fetch default --model-set default --save-load default --train default
```
#### Tune
```shell
$ dong_mnist_example --do-tune
```
Which uses default modules.
And here is the equivalent command
```shell
$ dong_mnist_example --do-tune --data-fetch default --model-set default --save-load default --train default --tune default
```

