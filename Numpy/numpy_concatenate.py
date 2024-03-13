import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a)
print(b)
print(np.concatenate((a, b), axis = 1))
print(np.concatenate((a, b), axis = 0))