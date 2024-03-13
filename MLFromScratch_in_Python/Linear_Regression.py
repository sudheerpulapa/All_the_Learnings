import numpy as np
import math
import matplotlib.pyplot as plt

class Regression(object):
    """Base regression model. Models the relationship between a scalar dependent variable y and the independent 
    variables X. 
    Parameters:
    -----------
    n_iterations: int
        The number of training iterations the algorithm will tune the weights for.
    learning_rate: float
        The step length that will be used when updating the weights.
    """
    def __init__(self, n_iterations, learning_rate):
        self.n_iterations = n_iterations
        self.learning_rate = learning_rate

    def initialize_weights(self, n_features):
        """Initialize weights randomly [-1/N, 1/N] """
        limit = 1 / math.sqrt(n_features)
        self.w = np.random.uniform(-limit, limit, (n_features, 1))

    def fit(self, X, y):
        # Insert constant ones for bias weights
        X = np.insert(X, 0, 1, axis=1)
        self.training_errors = []
        self.initialize_weights(n_features=X.shape[1])

        # Do gradient descent for n_iterations
        for i in range(self.n_iterations):
            y_pred = X.dot(self.w)
            # Calculate l2 loss
            mse = np.mean(0.5 * (y - y_pred)**2)
            self.training_errors.append(mse)
            # Gradient of l2 loss w.r.t w
            grad_w = -X.T.dot(y - y_pred) / len(y)
            # Update the weights
            self.w -= self.learning_rate * grad_w

    def predict(self, X):
        # Insert constant ones for bias weights
        X = np.insert(X, 0, 1, axis=1)
        y_pred = X.dot(self.w)
        return y_pred

class LinearRegression(Regression):
    """Linear model.
    Parameters:
    -----------
    n_iterations: int
        The number of training iterations the algorithm will tune the weights for.
    learning_rate: float
        The step length that will be used when updating the weights.
    """
    def __init__(self, n_iterations=100, learning_rate=0.001):
        super(LinearRegression, self).__init__(n_iterations=n_iterations,
                                                learning_rate=learning_rate)

# Generate random data
np.random.seed(42)
X = np.random.randn(100, 1)  # Random input data
y = 3 * X + 2 + np.random.randn(100, 1) * 0.1  # Random output data with noise

# Fit the linear regression model
model = LinearRegression(n_iterations=1000, learning_rate=0.01)
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Plotting the results
plt.scatter(X, y, label='Original data')
sorted_indices = np.argsort(X.flatten())
plt.plot(X[sorted_indices], y_pred[sorted_indices], 'r-', label='Fitted line')
plt.legend()
plt.title('Linear Regression with Random Data')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
