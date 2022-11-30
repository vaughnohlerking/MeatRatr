# MeatRatr

Machine learning algorithm for classifying the quality of meat based on marbling, freshness, etc.

required libraries setup:

# Requires the latest pip

pip install --upgrade pip

# Current stable release for CPU and GPU

pip install tensorflow

# to train data

$ python fine_tune.py root/ classes.txt <result_root> [epochs_pre] [epochs_fine] [batch_size_pre] [batch_size_fine] [lr_pre] [lr_fine] [snapshot_period_pre] [snapshot_period_fine]
python3 src/otXception/fine_tune.py root/ classes.txt src/otXception/output

# to test data

$ python inference.py result/model_fine_final.h5 classes.txt images/airplane.jpg
python3 src/otXception/inference.py src/otXception/output/model_fine_final.h5 testData/mid01.jpeg
