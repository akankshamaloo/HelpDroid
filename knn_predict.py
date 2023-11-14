import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import random
from sklearn.metrics import classification_report
from ar import *

def get_score():

    model_pkl_file = "knn_weight.pkl"  

    # load model from pickle file
    with open(model_pkl_file, 'rb') as file:  
        model = pickle.load(file)

    p=arduino()
    arr=[]
    arr.append(round(random.uniform(97.7,98.9),2))
    arr.append(p[0])
    arr.append(round(random.uniform(12,16),2))
    arr.append(round(random.uniform(100,120),2))
    arr.append(round(random.uniform(60,80),2))
    arr.append(p[1])

    print(arr)
    # evaluate model 
    sc = model.predict(arr)[0]
    print(sc)
    return sc


# check results
#print(classification_report(y_test, y_predict)) 