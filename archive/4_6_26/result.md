##  Notes:
Fourth iteration of testing. In this test weighted loss was applied to try to counter the imbalanced amount of images in each catagory to apply more weight to the lesser catagories
- Used a basic CNN with 3 convolutional layers and 2 fully connected layers. 
- Trained on Kaggle with a T4 GPU x2. 
- Dataset was about 9k images (6k packed snow, 1k dry, 1k ice, 1k mixed). 
- Trained with epoch 30, no other changes from previous training
- Model was trained from scratch and no pre-trained weights.


## Training loss summary
337.5s		Epoch 1 | Loss: 1.3819 | Time: 296.8s   
552.6s	 	Epoch 2 | Loss: 1.3434 | Time: 215.1s   
764.6s		Epoch 3 | Loss: 1.1985 | Time: 212.0s   
972.1s		Epoch 4 | Loss: 1.0974 | Time: 207.5s   
1186.5s		Epoch 5 | Loss: 1.0048 | Time: 214.4s   
1397.5s		Epoch 6 | Loss: 0.8916 | Time: 211.0s   
1604.7s		Epoch 7 | Loss: 0.8124 | Time: 207.2s   
1811.4s		Epoch 8 | Loss: 0.7246 | Time: 206.8s   
2025.2s		Epoch 9 | Loss: 0.6905 | Time: 213.8s   
2234.5s		Epoch 10 | Loss: 0.6658 | Time: 209.2s  
2445.6s		Epoch 11 | Loss: 0.6508 | Time: 211.2s  
2661.4s		Epoch 12 | Loss: 0.6323 | Time: 215.8s  
2875.8s		Epoch 13 | Loss: 0.6146 | Time: 214.4s  
3084.9s		Epoch 14 | Loss: 0.5934 | Time: 209.2s  
3294.6s		Epoch 15 | Loss: 0.5781 | Time: 209.7s  
3507.8s		Epoch 16 | Loss: 0.5632 | Time: 213.2s  
3717.9s		Epoch 17 | Loss: 0.5193 | Time: 210.1s  
3930.7s		Epoch 18 | Loss: 0.5054 | Time: 212.8s  
4143.0s		Epoch 19 | Loss: 0.4376 | Time: 212.3s  
4353.8s		Epoch 20 | Loss: 0.4083 | Time: 210.8s  
4566.6s		Epoch 21 | Loss: 0.3951 | Time: 212.8s  
4778.4s		Epoch 22 | Loss: 0.3733 | Time: 211.8s  
4995.4s		Epoch 23 | Loss: 0.3444 | Time: 217.0s  
5209.3s		Epoch 24 | Loss: 0.3145 | Time: 213.9s  
5424.0s		Epoch 25 | Loss: 0.3075 | Time: 214.7s  
5641.9s		Epoch 26 | Loss: 0.3204 | Time: 217.9s  
5857.7s		Epoch 27 | Loss: 0.3079 | Time: 215.8s  
6075.8s		Epoch 28 | Loss: 0.2858 | Time: 218.1s  
6294.5s		Epoch 29 | Loss: 0.2953 | Time: 218.7s  
6511.2s		Epoch 30 | Loss: 0.2790 | Time: 216.7s  

Compared to the previous training there is significant diffrence in the loss progression


## Results:
Test Set Results:
Overall: 742/804  Accuracy: 92.3%
  dry: 66/78  Accuracy: 84.6%
  ice: 75/75  Accuracy: 100.0%
  mixed: 43/61  Accuracy: 70.5%
  snow: 558/590  Accuracy: 94.6%


Testing on 60 external images
External CV Images Results:
Overall: 10/60  Accuracy: 16.7%
  dry: 1/15  Accuracy: 6.7%
  ice: 2/15  Accuracy: 13.3%
  mixed: 1/15  Accuracy: 6.7%
  snow: 6/15  Accuracy: 40.0% 


The results show the model is the unproprtional amount of images did skew the results a bit and now the model is able to predict all the catagories with decent accrucy. The issue of many of the images being similar is problem that is still present, likely causing it to fail the cross validation tests. Applying image transformation may help get around the issue of limited image data and increase the correct predictions on the cross validation.