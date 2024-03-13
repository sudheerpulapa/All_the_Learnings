import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Compute the mean of all elements in the array
mean_value = np.mean(arr)
print("Mean:", mean_value)

# Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Compute the mean along the columns (axis=0)
mean_columnwise = np.mean(arr_2d, axis=0)
print("Mean along columns:", mean_columnwise)

# Compute the mean along the rows (axis=1)
mean_rowwise = np.mean(arr_2d, axis=1)
print("Mean along rows:", mean_rowwise)
