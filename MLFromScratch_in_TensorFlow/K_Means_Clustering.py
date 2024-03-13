import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Generate some random data points
num_points = 200
num_clusters = 3
points = np.random.randn(num_points, 2).astype(np.float32) * 0.5

# Initialize centroids randomly
centroids = tf.Variable(points[np.random.choice(num_points, num_clusters)], dtype=tf.float32)

# TensorFlow graph input
points_placeholder = tf.Variable(points, dtype=tf.float32)

# Assign each point to the closest centroid
assignments = tf.argmin(tf.reduce_sum(tf.square(tf.expand_dims(points_placeholder, 1) - centroids), axis=2), axis=1)

# Update centroids by taking the mean of all points assigned to each centroid
means = []
for c in range(num_clusters):
    means.append(tf.reduce_mean(tf.gather(points_placeholder, tf.reshape(tf.where(tf.equal(assignments, c)), [1, -1])), axis=[1]))
new_centroids = tf.concat(means, axis=0)

# Update centroids by taking the mean of all points assigned to each centroid
update_centroids = centroids.assign(new_centroids)

# Initialize TensorFlow session
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Run k-Means algorithm
for step in range(100):
    _, centroid_values, assignment_values = sess.run([update_centroids, centroids, assignments])

# Plot the clustered data points and centroids
plt.scatter(points[:, 0], points[:, 1], c=assignment_values, s=50, alpha=0.5)
plt.plot(centroid_values[:, 0], centroid_values[:, 1], 'kx', markersize=15)
plt.title('k-Means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
