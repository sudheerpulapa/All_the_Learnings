from numpy.linalg import inv
import numpy as np

a = np.array([
    [1., 2.],
    [3., 4.]
])

ainv = inv(a) 
print(ainv)
print(np.dot(ainv, a))
print(np.eye(2))
print(np.allclose(np.dot(a, ainv), np.eye(2)))


