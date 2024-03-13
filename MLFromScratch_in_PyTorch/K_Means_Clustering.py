import torch
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
X = np.random.rand(100, 2)

# Convert numpy array to PyTorch tensor
X_tensor = torch.tensor(X, dtype=torch.float32)

# Define the number of clusters
k = 3

# Initialize centroids randomly
centroids = X_tensor[np.random.choice(X_tensor.shape[0], k, replace=False)]

# Perform k-means clustering
max_iters = 100
for _ in range(max_iters):
    distances = torch.sqrt(((X_tensor.unsqueeze(1) - centroids.unsqueeze(0))**2).sum(dim=2))
    labels = torch.argmin(distances, dim=1)
    new_centroids = torch.stack([X_tensor[labels == i].mean(dim=0) for i in range(k)])
    if torch.all(torch.eq(centroids, new_centroids)):
        break
    centroids = new_centroids

# Convert centroids and labels to numpy arrays
centroids = centroids.detach().numpy()
labels = labels.numpy()

# Plotting the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='red', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()
plt.show()
