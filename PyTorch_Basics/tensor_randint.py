import torch

# Generate a random integer tensor of size (3, 4) in the range [0, 10)
random_tensor = torch.randint(low=0, high=10, size=(3, 4))

print("Random Tensor:")
print(random_tensor)
