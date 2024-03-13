import torch 

# ==================================================== # 
#                  Initializing Tensor                 #
# ==================================================== #

device = "cuda" if torch.cuda.is_available() else "cpu"

my_tensor = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
], dtype=torch.float32, device=device, requires_grad=True)

print("Initialized Tensor:")
print(my_tensor)  # Prints the initialized tensor
print("Data Type (dtype):")
print(my_tensor.dtype)  # Prints the data type of the tensor
print("Device:")
print(my_tensor.device)  # Prints the device where the tensor is stored
print("Shape:")
print(my_tensor.shape)  # Prints the shape of the tensor
print("Requires Gradient:")
print(my_tensor.requires_grad)  # Prints whether gradient computation is enabled for the tensor

# Other common initialization methods 
print("Empty Tensor:")
x = torch.empty(size=(3, 3))  # Uninitialized tensor with shape (3, 3)
print(x)

print("Zero-filled Tensor:")
x = torch.zeros((3, 3))  # Tensor filled with zeros with shape (3, 3)
print(x)

print("Random Tensor:")
x = torch.rand((3, 3))  # Randomly initialized tensor with shape (3, 3)
print(x)

print("Tensor of Ones:")
x = torch.ones((3, 3))  # Tensor filled with ones with shape (3, 3)
print(x)

print("Identity Matrix Tensor:")
x = torch.eye(5, 5)  # Identity matrix tensor with shape (5, 5)
print(x)

print("Tensor with Values from 0 to 4:")
x = torch.arange(start=0, end=5, step=1)  # Tensor containing values from 0 to 4
print(x)

print("Tensor with 10 Equally Spaced Points between 0.1 and 1:")
x = torch.linspace(start=0.1, end=1, steps=10)  # Tensor with 10 equally spaced points between 0.1 and 1
print(x)

print("Tensor Sampled from Normal Distribution:")
x = torch.empty(size=(1, 5)).normal_(mean=0, std=1)  # Tensor with values sampled from a normal distribution
print(x)

print("Tensor Sampled from Uniform Distribution between 0 and 1:")
x = torch.empty(size=(1, 5)).uniform_(0, 1)  # Tensor with values sampled from a uniform distribution between 0 and 1
print(x)

print("Tensor with Ones on the Diagonal and Zeros Elsewhere:")
x = torch.diag(torch.ones(3))  # Tensor with ones on the diagonal and zeros elsewhere
print(x)

# How to initialize and convert tensors to other types (int, float, double)
tensor = torch.arange(4)  # Tensor containing values from 0 to 3
print("Boolean Tensor:")
print(tensor.bool())  # Converts tensor to boolean data type
print("Short Tensor:")
print(tensor.short())  # Converts tensor to 16-bit integer data type (short)
print("Long Tensor:")
print(tensor.long())  # Converts tensor to 64-bit integer data type (long)
print("Half Tensor:")
print(tensor.half())  # Converts tensor to 16-bit floating point data type (half)
print("Float Tensor:")
print(tensor.float())  # Converts tensor to 32-bit floating point data type (float)
print("Double Tensor:")
print(tensor.double())  # Converts tensor to 64-bit floating point data type (double)

# Array to Tensor conversion and vice-versa 
import numpy as np
np_array = np.zeros((5, 5))  # 5x5 array filled with zeros
print("Numpy Array:")
print(np_array)  # Print numpy array
tensor = torch.from_numpy(np_array)  # Convert numpy array to tensor
print("Converted to Tensor:")
print(tensor)  # Print converted tensor
np_array_back = tensor.numpy()  # Convert tensor back to numpy array
print("Converted Back to Numpy Array:")
print(np_array_back)  # Print converted numpy array