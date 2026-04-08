##  Notes:
This was a test with a pretrained model to see how the models being created fair against it as a baseline/cap. The original structure was made by Pierce Newell
- Used a pretrained vgg16 model
- Trained on Kaggle with a T4 GPU x2. 
- Dataset was about 9k images (6k packed snow, 1k dry, 1k ice, 1k mixed). 
- Trained with epoch 10


## Training loss summary
Epoch 1 | Loss: 0.1037 | Time: 268.9s 
Epoch 2 | Loss: 0.0377 | Time: 213.5s 
Epoch 3 | Loss: 0.0308 | Time: 210.5s 
Epoch 4 | Loss: 0.0269 | Time: 223.3s 
Epoch 5 | Loss: 0.0224 | Time: 216.0s 
Epoch 6 | Loss: 0.0211 | Time: 219.1s 
Epoch 7 | Loss: 0.0204 | Time: 218.2s 
Epoch 8 | Loss: 0.0272 | Time: 216.7s 
Epoch 9 | Loss: 0.0377 | Time: 217.6s 
Epoch 10 | Loss: 0.0300 | Time: 218.0s  

The model seems to already reach the most it can learn at epoch 7, this is supported by the idea that the pretrained model doesn't need to learn how to detect features and only what the catagories we want are.


## Results:
Test Set Results:
Overall: 791/804  Accuracy: 98.4%   
dry: 76/78  Accuracy: 97.4%   
ice: 75/75  Accuracy: 100.0%  
mixed: 54/61  Accuracy: 88.5%  
snow: 586/590  Accuracy: 99.3%   

External CV Images Results:
Overall: 22/60  Accuracy: 36.7% 
dry: 1/15  Accuracy: 6.7% 
ice: 7/15  Accuracy: 46.7%  
mixed: 1/15  Accuracy: 6.7% 
snow: 13/15  Accuracy: 86.7%  


These results show that our data overall can only train a model to become a bit better than random at predicting the road conditions and about 33-40% on CV.