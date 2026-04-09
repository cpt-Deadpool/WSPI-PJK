##  Notes:
Fith iteration of testing. In this test augmentation was applied to try to counter the amount of similar images with variations so the model would not learn just the patterns of the few images. 
- Used a basic CNN with 3 convolutional layers and 2 fully connected layers. 
- Trained on Kaggle with a T4 GPU x2. 
- Dataset was about 9k images (6k packed snow, 1k dry, 1k ice, 1k mixed). 
- Trained with epoch 50
- Model was trained from scratch and no pre-trained weights.


## Training loss summary
324.1s		Epoch 1 | Loss: 1.3789 | Time: 289.7s
557.6s		Epoch 2 | Loss: 1.3268 | Time: 233.5s
786.7s		Epoch 3 | Loss: 1.2509 | Time: 229.1s
1014.3s		Epoch 4 | Loss: 1.2222 | Time: 227.6s
1244.0s		Epoch 5 | Loss: 1.1882 | Time: 229.7s
1473.3s		Epoch 6 | Loss: 1.0732 | Time: 229.4s
1702.8s		Epoch 7 | Loss: 0.9693 | Time: 229.4s
1935.5s		Epoch 8 | Loss: 0.8250 | Time: 232.7s
2161.8s		Epoch 9 | Loss: 0.7978 | Time: 226.3s
2391.9s		Epoch 10 | Loss: 0.7549 | Time: 230.1s
2622.6s		Epoch 11 | Loss: 0.7463 | Time: 230.7s
2855.0s		Epoch 12 | Loss: 0.7404 | Time: 232.4s
3084.5s		Epoch 13 | Loss: 0.7532 | Time: 229.5s
3313.2s		Epoch 14 | Loss: 0.7237 | Time: 228.7s
3542.5s		Epoch 15 | Loss: 0.7259 | Time: 229.3s
3772.2s		Epoch 16 | Loss: 0.7205 | Time: 229.8s
3999.7s		Epoch 17 | Loss: 0.7144 | Time: 227.5s
4230.7s		Epoch 18 | Loss: 0.6945 | Time: 230.9s
4460.0s		Epoch 19 | Loss: 0.7020 | Time: 229.3s
4686.4s		Epoch 20 | Loss: 0.6895 | Time: 226.4s
4914.3s		Epoch 21 | Loss: 0.6922 | Time: 227.9s
5141.7s		Epoch 22 | Loss: 0.6877 | Time: 227.4s
5375.1s		Epoch 23 | Loss: 0.6862 | Time: 233.4s
5601.2s		Epoch 24 | Loss: 0.6755 | Time: 226.2s
5829.7s		Epoch 25 | Loss: 0.6938 | Time: 228.5s
6056.9s		Epoch 26 | Loss: 0.6629 | Time: 227.2s
6284.6s		Epoch 27 | Loss: 0.6447 | Time: 227.7s
6514.1s		Epoch 28 | Loss: 0.6252 | Time: 229.6s
6746.2s		Epoch 29 | Loss: 0.6102 | Time: 232.0s
6969.1s		Epoch 30 | Loss: 0.5970 | Time: 222.9s
7198.8s		Epoch 31 | Loss: 0.5707 | Time: 229.7s
7433.8s		Epoch 32 | Loss: 0.5501 | Time: 235.0s
7663.3s		Epoch 33 | Loss: 0.5328 | Time: 229.5s
7895.5s		Epoch 34 | Loss: 0.5200 | Time: 232.2s
8127.9s		Epoch 35 | Loss: 0.4992 | Time: 232.4s
8351.5s		Epoch 36 | Loss: 0.5001 | Time: 223.6s
8578.9s		Epoch 37 | Loss: 0.4816 | Time: 227.4s
8810.5s		Epoch 38 | Loss: 0.4948 | Time: 231.6s
9033.3s		Epoch 39 | Loss: 0.4650 | Time: 222.8s
9259.6s		Epoch 40 | Loss: 0.4378 | Time: 226.3s
9490.3s		Epoch 41 | Loss: 0.4618 | Time: 230.8s
9717.6s		Epoch 42 | Loss: 0.4439 | Time: 227.3s
9945.7s		Epoch 43 | Loss: 0.4239 | Time: 228.1s
10176.5s	Epoch 44 | Loss: 0.4227 | Time: 230.8s
10404.7s	Epoch 45 | Loss: 0.4152 | Time: 228.1s
10638.7s	Epoch 46 | Loss: 0.3937 | Time: 234.1s
10866.4s	Epoch 47 | Loss: 0.3890 | Time: 227.6s
11090.6s	Epoch 48 | Loss: 0.4013 | Time: 224.3s
11318.0s	Epoch 49 | Loss: 0.3839 | Time: 227.4s
11546.8s	Epoch 50 | Loss: 0.3810 | Time: 228.8s

There is nothing special about the loss progression this time around, it simpily reached the limit of it's training ar around epoch 47.


## Results:
Test Set Results:
Overall: 605/804  Accuracy: 75.2%
  dry: 72/78  Accuracy: 92.3%
  ice: 75/75  Accuracy: 100.0%
  mixed: 45/61  Accuracy: 73.8%
  snow: 413/590  Accuracy: 70.0%

Testing on 60 external images
External CV Images Results:
Overall: 20/60  Accuracy: 33.3%
  dry: 6/15  Accuracy: 40.0%
  ice: 1/15  Accuracy: 6.7%
  mixed: 5/15  Accuracy: 33.3%
  snow: 8/15  Accuracy: 53.3%


The results show that augmentation allowed the model to handle the cross validation data better, but showed that it also significantly dropped it's ability to predict the non augmented test data. Removing cropping may help sinceit was accidently left in. Dropout of nodes may help as well prevent even more memorization.