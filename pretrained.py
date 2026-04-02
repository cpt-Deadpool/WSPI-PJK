from torchvision import models
from torchvision.models import VGG16_Weights
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch

model = models.vgg16(weights=VGG16_Weights.DEFAULT)
model.classifier[6] = nn.Linear(4096, 4)

for param in model.parameters():
    param.requires_grad = False

for param in model.classifier.parameters():
    param.requires_grad = True


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229, 0.224, 0.225]
        )
    ])
# change the image folder to match yours :)
train_dataset = datasets.ImageFolder("/media/pierce/BA79-9A67/train", transform = transform)
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.classifier.parameters(), lr = 0.001)

model.train()

num_epochs = 5

for epoch in range(num_epochs):
    running_loss = 0.0

    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {running_loss / len(train_loader):.4f}")

correct = 0
total = 0

model.eval()
with torch.no_grad():
    for images, labels in train_loader:
        outputs = model(images)
        _, predicted = outputs.max(1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total:.2f}%")

torch.save(model.state_dict(), "vgg_model.pth")
