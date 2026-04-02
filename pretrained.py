import numpy as np
from PIL import Image

import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.transforms as transforms
from torchvision import models
from torchvision.models import VGG16_Weights
from torchvision import datasets

import os
import torchvision.transforms.functional as TF

from torch.utils.data import random_split, DataLoader

#pull the pretrained vgg model and change the last classifier to handle 4 classes 
#(snow, mixed, ice, dry)
model = models.vgg16(weights=VGG16_Weights.DEFAULT)
model.classifier[6] = nn.Linear(4096, 4)

#the vgg model contains millions of params, turn all fo them off :)
for param in model.parameters():
    param.requires_grad = False

#only turn on the params for our classifier, its better for image classification
for param in model.classifier.parameters():
    param.requires_grad = True

class RoadDataset(datasets.ImageFolder):
    def __getitem__(self, index):
        # 1. Get the path, image, and label
        path, label_idx = self.samples[index]
        image = self.loader(path) # Loads as PIL Image
        
        filename = os.path.basename(path)
        condition = self.classes[label_idx] 

        width, height = image.size

        if "arenacam" in filename:
            # Car hood in image
            image = TF.crop(image, top=700, left=1200, height=400, width=400)
        elif "pylon_camera" in filename:
            # No car hood in view
            image = TF.crop(image, top=400, left=800, height=400, width=400)
        elif width < 400:
            pass #dont crop images that are too small
        else:
            #base case just in case
            image = TF.center_crop(image, (400, 400))

        # apply transforms (resize, tensor, normalize)
        if self.transform is not None:
            image = self.transform(image)

        # Returns: (image, index of label)
        return image, label_idx
    
    def get_classes(self):
        return self.classes

#the vgg model expects a specific size, i havent checked if this results in a 'correct' image of the road
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229, 0.224, 0.225]
        )
    ])
#ImageFolder grabs the images from your specified location and creates labels automatically. 
# change the image folder to match yours :)
train_dataset = RoadDataset("/media/pierce/BA79-9A67/train", transform = transform)
#only train on batches of 32 images at a time, can be changed 
train_loader = DataLoader(train_dataset, batch_size = 32, shuffle = True)

#this is how we manage and calculate loss
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.classifier.parameters(), lr = 0.001)

model.train()

#num of times we train the model
num_epochs = 5
#train!
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

#Evaluates the model after training all epochs
model.eval()
with torch.no_grad():
    for images, labels in train_loader:
        outputs = model(images)
        _, predicted = outputs.max(1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Accuracy: {100 * correct / total:.2f}%")

torch.save(model.state_dict(), "vgg_model.pth")
