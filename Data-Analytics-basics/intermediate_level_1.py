'''
1. Load Data
2. Define Model

3. Define Loss
4. Forward Pass
5. Backward Pass
6. Update Weights
7. Repeat
'''

'''
Image
  ↓
Forward Pass (Guess)
  ↓
Loss (Check Mistake)
  ↓
Backward Pass (Find Error Source)
  ↓
Update Weights (Fix Brain)
  ↓
Repeat
'''



import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 1️⃣ Load dataset


transform = transforms.ToTensor()

train_data = datasets.MNIST(root='./data',
                            train=True,
                            download=True,
                            transform=transform)


train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# 2️⃣ Simple Neural Network 
# Is nn.Sequential a Mathematical Formula?

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)


# 3️⃣ Loss and Optimizer
# This is a statistical error function.

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4️⃣ Training (only 1 epoch for simplicity)
for images, labels in train_loader:
    outputs = model(images)
    loss = loss_fn(outputs, labels)
    
    '''
    optimizer.zero_grad()  → Reset previous gradients
    loss.backward()        → Calculate gradients
    optimizer.step()       → Update weights
    '''

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Training Done ✅")


'''
| Model (nn.Sequential) | Loss Function              |
| --------------------- | -------------------------- |
| Makes prediction      | Measures mistake           |
| Mathematical mapping  | Statistical evaluation     |
| Forward computation   | Error computation          |
| Defines structure     | Defines learning objective |
'''


