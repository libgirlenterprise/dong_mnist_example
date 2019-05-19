# tabemasu : a dong train exec sample project
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
USAGE: tabemasu [OPTIONS]

OPTIONS:

   --data-fetch: the module handling data fetching

   --model-set: the module indicating a model set
   
   --save-load: the module handling model serialization/deserialization
   
   --train: the module of training program
```
### Sample Command
```shell
$ tabemasu 
```
Which uses default modules.
And here is the equivalent command
```shell
$ tabemasu --data-fetch default --model-set default --save-load default --train default
```
