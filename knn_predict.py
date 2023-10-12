import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
from sklearn.metrics import classification_report



model_pkl_file = "knn_weight.pkl"  

# load model from pickle file
with open(model_pkl_file, 'rb') as file:  
    model = pickle.load(file)

arr=[100.6,107,18,136,68,98]

# evaluate model 
print(model.predict(arr)[0])

# check results
#print(classification_report(y_test, y_predict)) 