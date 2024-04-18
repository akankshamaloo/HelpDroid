import numpy as np
from collections import Counter
cnt=0

def euclidean_distance(x1, x2):

    x1 = np.array(x1, dtype=np.float64)  # Ensure x1 is a NumPy array with a compatible data type
    x2 = np.array(x2, dtype=np.float64)  # Ensure x2 is a NumPy array with a compatible data type

    distance = np.sqrt(np.sum((x1 - x2) ** 2))

    return distance


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        #print(X)
        predictions = [self._predict(X)]
        return predictions

    def _predict(self, x):
        # compute the distance
        global cnt
        #print(x," ",cnt)
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        cnt+=1
        # get the closest k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # majority voye
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]