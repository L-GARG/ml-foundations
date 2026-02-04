import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [2,3,4]])
w = np.array([0.1, 0.2, 0.3])
b = 0.5 

y_pred = x @ w + b
print(y_pred)

y = np.array([2, 4, 6, 2.7])

loss = np.mean((y_pred - y) ** 2)
print(loss*100)