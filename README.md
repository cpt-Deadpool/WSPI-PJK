# WSPI-PJK
ML Project CS 5821

ML Road Classification

Project statement: 
Classify images of road surfaces into categories based on road conditions

Categories: 
Dry surface
Packed snow
Mixed snow over ice
White ice
Black ice
Tentatively can combine white and black if the split is not feasible

Strategies: 
Supervised
Label images, it can be done in blocks based on day and location
Unsupervised
Not quite sure yet, need to do some research


Decided Training Strategy:
We will use supervised learning since it is the only way for the model to properly determine if an image is a certain category we define, otherwise it would group based on whatever it detects as similar qualities and not the specific aspects of the categories we want. 

Labeling:
To label the images for supervised learning we will manually categorize the images into folders for each category. In this process we learned how the provided data is lacking in some categories and that we would have to supplement the data from online and our own pictures.

Training:
To train the model we will be making it all from scratch to learn the process rather than use a pretrained model. To verify it is running well and to see efficiency we will compare our results from the from scratch model with the pretrained on.






