# Group Project - Object_detection for cocacola and pepsi

This repository contains the code and documentation for our group project on object detection for CocaCola and Pepsi cans or bottles using computer vision techniques and deploying the trained model to a Raspberry Pi.


## Tasks


### Task 1: Data Acquisition

In this task, we searched and acquired the dataset for our project through the Kaggle website. We have chosen the Pepsi and CocaCola dataset as our primary dataset. The dataset can be obtained from https://www.kaggle.com/datasets/die9origephit/pepsi-and-cocacola-images. that include 200 images of Pepsi and 200 images of Coca-Cola.


### Task 2: Data Preparation - Dataset Labeling and Augmentation

For this task, we used Roboflow to label and annotate the acquired dataset. Additionally, we applied computer vision techniques such as rotation, flipping, shearing, etc., to augment the images and create a larger and more diverse dataset. The augmented dataset was then split into train, test, and validation sets with the following ratio:
- Training set: 70%
- Test set: 10%
- Validation set: 20%


### Task 3: Model Training and deploy

In this task, we utilized the YOLOv8 model for object detection. We downloaded the model code snippet from Roboflow and incorporated it into our project. The model was trained using the augmented dataset with the following configuration:
- Epochs: 100
- Image Size: 840

From the trained dataset, be able to receive a trained model name ‘best.pt’ that will be used for classification model to predict the result of the detected object. We further apply our trained object detection model by counting the number of detected objects within a frame.


### Task 4: Model Inference - Model Deployment to Raspberry Pi

The final task involved deploying the trained object detection model to a Raspberry Pi. The Raspberry Pi was set up to detect CocaCola and Pepsi cans or bottles in real-time using the deployed model.

First, the Raspberry Pi OS is set up into an SD Card to be used for the small single-board computer as an operating system. After attaching all necessary components to the small single-board computer, essential libraries are installed such as numpy, opencv, and YOLO. The terminal is then used to create python scripts for the object detection code that will be run for object classification.

