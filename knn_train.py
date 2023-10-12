import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from HelpDroid.knn import KNN
import pandas as pd
import pickle

cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])

score_df = pd.read_csv('patient_data.csv', header=0)
for col in score_df.columns:
    if col != 'SCORE':
        score_df[col] = pd.to_numeric(score_df[col])
    else:
        score_df[col] = score_df[col].astype('int')
score_df = score_df.rename(columns={'SCORE ':'SCORE'})
X = score_df.drop('SCORE',axis=1)
y = score_df.SCORE

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

X_train = X_train.to_numpy()
y_train= y_train.to_numpy()
X_test=X_test.to_numpy()
y_test=y_test.to_numpy()

clf = KNN(k=5)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print(predictions)

acc = np.sum(predictions == y_test) / len(y_test)
print(acc)



# save the iris classification model as a pickle file
model_pkl_file = "knn_weight.pkl"  

with open(model_pkl_file, 'wb') as file:  
    pickle.dump(clf, file)