import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Generating random data
torch.manual_seed(42)  # for reproducibility
X = torch.randn(100, 1)  # random input data
y = 3 * X + 2 + torch.randn(100, 1) * 0.1  # random output data with some noise

# Define the model
class LinearRegression(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)
        
    def forward(self, x):
        return self.linear(x)

input_size = 1  # number of features
output_size = 1  # number of output classes
model = LinearRegression(input_size, output_size)

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training the model
num_epochs = 100
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)
    
    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Plotting the results
predicted = model(X).detach().numpy()
plt.scatter(X.numpy(), y.numpy(), label='Original data')
plt.plot(X.numpy(), predicted, 'r-', label='Fitted line')
plt.legend()
plt.show()
