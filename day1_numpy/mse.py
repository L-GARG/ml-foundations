import numpy as np

def mse(y_true, y_pred):
    x = (y_true-y_pred)**2

    return np.sum(x)/len(x)

y_true = np.array([1,2,3,4,5])
y_pred = np.array([0,1,2,3,4])

print(mse(y_true, y_pred))