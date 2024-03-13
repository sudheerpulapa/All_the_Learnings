import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
X = np.random.rand(6, 2)

print(X.round(2))
print()
centroids = X[np.random.choice(X.shape[0], 3, replace = False)]
print(centroids.round(2))
print()
print(X)
print()
print(centroids[:, np.newaxis])

