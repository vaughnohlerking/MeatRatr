# MeatRatr

Machine learning algorithm for classifying the quality of meat based on marbling, freshness, etc.

main algorithm is using @otenim 's implementation of Xception CNN. Github repo https://github.com/otenim/Xception-with-Your-Own-Dataset
This repo has a much better README and describes all the ways to use and configure it.

## Requires some libraries

anaconda
tensorflow
keras
selenium
matplotlib

## to train data

$ python3 src/{ model folder name }/fine_tune.py data/ classes.txt src/{ model folder name }/output
example use
$ python3 src/customCNN/fine_tune.py data/ classes.txt src/customCNN/output

## to test data

$ python3 src/{ model folder name }/inference.py src/{ model folder name }/output/model_fine_final.h5 classes.txt testData/{ name of test meat pic}
example use
$ python3 src/customCNN/inference.py src/customCNN/output/model_fine_final.h5 classes.txt testData/mid01.jpeg

## output

The output will be put under the folder of the respective model. For example the output of customCNN is under src/customCNN/output. Inside there will be two png's describing the accuracy and the loss
