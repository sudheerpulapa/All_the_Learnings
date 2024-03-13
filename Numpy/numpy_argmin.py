import numpy as np

# Create a 2D array
arr = np.array([[11, 2, 3],
                [4, 57, 6],
                [17, 8, 9]])

# Find the index of the minimum value in the entire array
min_index = np.argmin(arr)
print("Index of the minimum value in the entire array:", min_index)

# Find the indices of the minimum values along each column
min_indices_columnwise = np.argmin(arr, axis=0)
print("Indices of the minimum values along each column:", min_indices_columnwise)

# Find the indices of the minimum values along each row
min_indices_rowwise = np.argmin(arr, axis=1)
print("Indices of the minimum values along each row:", min_indices_rowwise)
