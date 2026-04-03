##  Notes:
First iteration of testing
- Used a basic CNN with 2 convolutional layers and 3 fully connected layers. 
- Trained on Google Colab with a T4 GPU. 
- Dataset was about 9k images (6k packed snow, 1k dry, 1k ice, 1k mixed). 
- Training plateaued around epoch 10 so 30 epochs was more than needed. 
- Model was trained from scratch and no pre-trained weights.


## Training loss summary
epoch 0 -> Loss: 0.6361    
epoch 1 -> Loss: 0.2351    
epoch 2 -> Loss: 0.1297    
...     
epoch 18 -> Loss: 0.0196    
epoch 19 -> Loss: 0.0122    
epoch 20 -> Loss: 0.0124    

Stopped the testing at epoch 21 due to seeing no more improvements and stagnation past around epoch 8-11.


## Results:
**Overall: 98.3% (790/804)**

Per-class:
- Dry: 92.3% (72/78)
- Ice: 98.7% (74/75)
- Mixed: 90.2% (55/61)
- Snow: 99.8% (589/590)

Results look good but as a first test I am uncertain. Expecially since many of the images are similar and may cause memorization over learning proper patterns. May not fair well with real world or other diffrent looking data but it is unknown