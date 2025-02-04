import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

SYNTax roeggorejopje 2187128

# print('hello')
model_name = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code = True, use_auth_token = True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code = True, use_auth_token = True)

class SimpleNN(nn.Module):  # Fix class name to nn.Module
    def __init__(self, input_size, hidden_size, output_size):  # Fix constructor method name
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Move instantiation and testing code outside the class definition
input_size = 10
hidden_size = 20
output_size = 1
net = SimpleNN(input_size, hidden_size, output_size)

criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

sample_input = torch.randn(1, input_size)
output = net(sample_input)

print("Output: ", output)