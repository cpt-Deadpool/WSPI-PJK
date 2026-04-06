##  Notes:
Second iteration of testing. Using the advice of Kyle Munger I reduced the amount of parameters handled from about 1 million to about 3 thousand. 
- Used a basic CNN with 3 convolutional layers and 2 fully connected layers. 
- Trained on Google Colab with a T4 GPU. 
- Dataset was about 9k images (6k packed snow, 1k dry, 1k ice, 1k mixed). 
- Training could still continue and improve past the the 10th epoch
- Model was trained from scratch and no pre-trained weights.


## Training loss summary
Epoch 1 | Loss: 0.9249 | Time: 352.8s
Epoch 2 | Loss: 0.6881 | Time: 350.5s
Epoch 3 | Loss: 0.6728 | Time: 345.1s
Epoch 4 | Loss: 0.6620 | Time: 346.1s
Epoch 5 | Loss: 0.6522 | Time: 344.3s
Epoch 6 | Loss: 0.6424 | Time: 344.6s
Epoch 7 | Loss: 0.6265 | Time: 348.2s
Epoch 8 | Loss: 0.6096 | Time: 354.6s
Epoch 9 | Loss: 0.5866 | Time: 350.5s
Epoch 10 | Loss: 0.5605 | Time: 351.7s

Only tested 10 epoch based on previous test being too much but with this new setup it was too little and the model could have become even better given a higher epoch


## Results:

Test Set Results:
Overall: 655/804  Accuracy: 81.5%
  dry: 0/78  Accuracy: 0.0%
  ice: 67/75  Accuracy: 89.3%
  mixed: 0/61  Accuracy: 0.0%
  snow: 588/590  Accuracy: 99.7%

Testing on 60 external images
External CV Images Results:
Overall: 15/60  Accuracy: 25.0%
  dry: 0/15  Accuracy: 0.0%
  ice: 2/15  Accuracy: 13.3%
  mixed: 0/15  Accuracy: 0.0%
  snow: 13/15  Accuracy: 86.7%


Results do not look very good but this is more of a good sign since it shows it is actually learning. to improve the results a higher epoch would be needed as well as analysis as to why it failed and struggled with dry and mixed.