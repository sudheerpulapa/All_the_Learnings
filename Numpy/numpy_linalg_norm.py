import numpy as np

# Define a vector
vector = np.array([3, 4])

# Calculate the Euclidean norm (L2 norm) of the vector
euclidean_norm = np.linalg.norm(vector)
print("Euclidean norm of the vector:", euclidean_norm)

# Calculate the Manhattan norm (L1 norm) of the vector
manhattan_norm = np.linalg.norm(vector, ord=1)
print("Manhattan norm of the vector:", manhattan_norm)
