# Face Recognition System using OpenCV and Deep Learning

This is an implementation of Face recognition and identification to implement an attendance system using a live video feed. 

## Setup

##### 1. Install and activate a virtualenv
    pip install virtualenv
    python3 -m virtualenv env
    source env/bin/activate
    
##### 2. Install Requirements
    pip3 install -r requirements.txt

##### 3. Generate Training Data [OPTIONAL]
The training data is the pictures of all the people whom you want to recognize. This script uses your webcam to capture 50 images continuously and store it in the `train_img` folder.
    
    python3 generate_data.py
    
##### 3. Preprocess data
The training data is now preprocessed with the faces being cropped and the faces are labelled here.

    python3 data_preprocess.py
   
##### 4. Model Training
The model is trained to extract the features from the face by using Haar Cascaders and the classes are labelled here. `classifier.py' contains the model which we are currently using. I currently use Linear SVM to predict the probability of a particular class

    python3 train_model.py

##### 5. Identify Face
This is the last part, where we try to identify a particular face by drawing a bounding box around it. The class with the highest probability for the image is shown as the label of the image. The current confidence threshhold is 70%, but this can be changed according to the preference of the user.
If the confidence is less than 70% then the face is not identified.

    python3 indentify_face_video.py

##### Credits:

1. FaceNet: A Unified Embedding for Face Recognition and Clustering, David Sandberg [Repo](https://github.com/davidsandberg/facenet)
2. A Discriminative Feature Learning Approach for Deep Face Recognition
3. Deep Face Recognition