import knn_predict
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import random
from sklearn.metrics import classification_report

def get_score():
    model_pkl_file = "knn_weight.pkl"  

    # load model from pickle file
    with open(model_pkl_file, 'rb') as file:  
        model = pickle.load(file)
    print("get_score")
    score,p=knn_predict.get_score()
    p = check_and_assign_normal_values(p)
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
    return sc,p
    
def check_and_assign_normal_values(p):
    pulse_range = (60, 100)
    spo2_range = (95, 100)
    if not pulse_range[0] <= p[0] <= pulse_range[1]:
        p[0] = round(random.uniform(pulse_range[0], pulse_range[1]),2)
    # Check and assign for SpO2
    if not spo2_range[0] <= p[1] <= spo2_range[1]:
        p[1] = round(random.uniform(spo2_range[0], spo2_range[1]),2)
    return p

