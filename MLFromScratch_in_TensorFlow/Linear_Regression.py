import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generating random data
np.random.seed(42)  # for reproducibility
X = np.random.randn(100, 1)  # random input data
y = 3 * X + 2 + np.random.randn(100, 1) * 0.1  # random output data with some noise

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Training the model
history = model.fit(X, y, epochs=100, verbose=0)

# Plotting the loss
plt.plot(history.history['loss'])
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()

# Plotting the results
plt.scatter(X, y, label='Original data')
plt.plot(X, model.predict(X), 'r-', label='Fitted line')
plt.legend()
plt.show()
