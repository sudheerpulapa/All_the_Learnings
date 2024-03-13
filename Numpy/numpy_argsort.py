import numpy as np

arr = np.array([3, 1, 2])
indices = np.argsort(arr)
print(indices)  # Output: [1 2 0]

# Use the indices to sort the original array
sorted_arr = arr[indices]
print(sorted_arr)  # Output: [1 2 3]
