import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
X = np.random.rand(100, 2)

# Implement k-means clustering from scratch
def k_means(X, k, max_iters=100, tol=1e-4):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    for _ in range(max_iters):
        distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        if np.linalg.norm(centroids - new_centroids) < tol:
            break
        centroids = new_centroids
    return centroids, labels

# Perform k-means clustering
k = 3
centroids, labels = k_means(X, k)

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='red', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()
plt.show()
