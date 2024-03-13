import numpy as np

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])

# Add a new axis to convert it into a 2-dimensional array
arr_2d = arr[:, np.newaxis]

print(arr_2d)
