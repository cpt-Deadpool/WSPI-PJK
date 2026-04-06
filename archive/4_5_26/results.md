##  Notes:
Third iteration of testing. Continuing with the reduction of parameters from about 1 million to about 3 thousand. 
- Used a basic CNN with 3 convolutional layers and 2 fully connected layers. 
- Trained on Kaggle with a T4 GPU x2. 
- Dataset was about 9k images (6k packed snow, 1k dry, 1k ice, 1k mixed). 
- Trained with epoch 30, no other changes from previous training
- Model was trained from scratch and no pre-trained weights.


## Training loss summary
286.2s		Epoch 1 | Loss: 0.9392 | Time: 256.4s   
496.3s		Epoch 2 | Loss: 0.6945 | Time: 210.0s   
713.8s		Epoch 3 | Loss: 0.6758 | Time: 217.5s   
933.4s		Epoch 4 | Loss: 0.6631 | Time: 219.6s   
1150.4s		Epoch 5 | Loss: 0.6537 | Time: 217.0s   
1360.7s		Epoch 6 | Loss: 0.6456 | Time: 210.3s   
1573.4s		Epoch 7 | Loss: 0.6355 | Time: 212.7s   
1790.1s		Epoch 8 | Loss: 0.6234 | Time: 216.7s   
2002.5s		Epoch 9 | Loss: 0.6107 | Time: 212.4s   
2215.9s		Epoch 10 | Loss: 0.5933 | Time: 213.4s  
2434.7s		Epoch 11 | Loss: 0.5750 | Time: 218.9s  
2650.3s		Epoch 12 | Loss: 0.5568 | Time: 215.6s  
2864.3s		Epoch 13 | Loss: 0.5407 | Time: 213.9s  
3074.7s		Epoch 14 | Loss: 0.5258 | Time: 210.4s  
3286.9s		Epoch 15 | Loss: 0.5107 | Time: 212.2s  
3499.1s		Epoch 16 | Loss: 0.4943 | Time: 212.2s  
3713.9s		Epoch 17 | Loss: 0.4838 | Time: 214.8s  
3928.0s		Epoch 18 | Loss: 0.4708 | Time: 214.1s  
4138.4s		Epoch 19 | Loss: 0.4590 | Time: 210.4s  
4351.2s		Epoch 20 | Loss: 0.4521 | Time: 212.8s  
4560.9s		Epoch 21 | Loss: 0.4441 | Time: 209.7s  
4778.5s		Epoch 22 | Loss: 0.4315 | Time: 217.6s  
4992.9s		Epoch 23 | Loss: 0.4198 | Time: 214.4s  
5202.6s		Epoch 24 | Loss: 0.3951 | Time: 209.7s  
5413.6s		Epoch 25 | Loss: 0.3728 | Time: 211.0s  
5627.4s		Epoch 26 | Loss: 0.3455 | Time: 213.8s  
5838.2s		Epoch 27 | Loss: 0.3185 | Time: 210.8s  
6049.7s		Epoch 28 | Loss: 0.3014 | Time: 211.5s  
6257.6s		Epoch 29 | Loss: 0.2806 | Time: 207.8s  
6465.6s		Epoch 30 | Loss: 0.2542 | Time: 208.0s  

I tested to epoch 30 based on previous training being limited by the small epoch. It seems the model is learning very well and gradually.


## Results:
Test Set Results:
Overall: 726/804  Accuracy: 90.3%   
- dry: 64/78  Accuracy: 82.1% 
- ice: 75/75  Accuracy: 100.0%    
- mixed: 1/61  Accuracy: 1.6% 
- snow: 586/590  Accuracy: 99.3%  

Testing on 60 external images   
External CV Images Results: 
Overall: 13/60  Accuracy: 21.7% 
- dry: 0/15  Accuracy: 0.0% 
- ice: 0/15  Accuracy: 0.0% 
- mixed: 0/15  Accuracy: 0.0%   
- snow: 13/15  Accuracy: 86.7%  


The results show the model is properly learning and that the increased epoch and reduced parameters have made a good impact. But the scores of the mixed with teh test set show that the model can't easily learn the mixed catagory easily. To improve the results applying weighted loss may help due to the 6k snow images skewing the results a lot. The issue of many of the images being similar is still a problem but can't currently be fixed. Applying image transformation may help as well to get around the issue of limited image data.