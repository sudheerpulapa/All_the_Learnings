import tensorflow as tf

# Suppose we have two tensors of numbers
tensor1 = tf.constant([1, 2, 3, 4, 5])
tensor2 = tf.constant([6, 7, 8, 9, 10])

# Adding the tensors using vectorization
result = tf.add(tensor1, tensor2)

print("Result of adding tensors using vectorization:")
print(result.numpy())  # Convert the TensorFlow tensor to a NumPy array for printing
