# MeatRatr

Machine learning algorithm for classifying the quality of meat based on marbling, freshness, etc.

main algorithm is using @otenim 's implementation of Xception CNN. Github repo https://github.com/otenim/Xception-with-Your-Own-Dataset
required libraries setup:

# Requires the latest pip and a ton of other libraries i'm not adding right now

pip install --upgrade pip

pip install tensorflow
pip install keras

# to train data

$ python fine_tune.py root/ classes.txt <result_root> [epochs_pre] [epochs_fine] [batch_size_pre] [batch_size_fine] [lr_pre] [lr_fine] [snapshot_period_pre] [snapshot_period_fine]
or
python3 src/otXception/fine_tune.py data/ classes.txt src/otXception/output

# to test data

$ python inference.py result/model_fine_final.h5 classes.txt images/airplane.jpg
or
python3 src/otXception/inference.py src/otXception/output/model_fine_final.h5 classes.txt testData/wagtest.png
