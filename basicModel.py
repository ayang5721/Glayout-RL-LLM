#This file is for a very simple neural network to get a bearing on the subject

import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):  # Fix class name to nn.Module
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(3,1)

    def forward(self, x):
        return self.fc1(x)
    
model = SimpleNN()

print("Initial weights: ", model.fc1.weight)   
print("Initial bias: ", model.fc1.bias)

criterion = nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=0.01)

x = torch.tensor([1.0,2.0,3.0])
target = torch.tensor([5.0])

for i in range(1000):
    optimizer.zero_grad()
    output = model(x)

    loss = criterion(output, target)

    loss.backward()

    optimizer.step()

    print("output: ", output)
    print("loss: ", loss.item())
