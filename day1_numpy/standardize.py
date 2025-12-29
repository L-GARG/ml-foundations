import numpy as np

def standardize(x):
    return (x-np.mean(x))/np.std(x)

x = np.array([11,29,37,45,53])
print(standardize(x))