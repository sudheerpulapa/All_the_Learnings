import numpy as np 

# Generating random data
np.random.seed(42)  # for reproducibility
X = np.random.randn(10, 1)  # random input data
y = 3 * X + 2 + np.random.randn(10, 1) * 0.1  # random output data with some noise

print(X.shape)
print(y.shape)

print(X.T)
print(y.T)