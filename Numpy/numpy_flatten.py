import numpy as np

# Create a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Flatten the array
flattened_arr = arr_2d.flatten()

print("Original array shape:", arr_2d.shape)
print("Flattened array:", flattened_arr)
print("Flattened array shape:", flattened_arr.shape)
