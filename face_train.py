import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"swap_image_train")
# print(image_dir)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Swapnil\\OpenCV_git_projects\\Cascades\\haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_id = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            # print(label, path)

            if not label in label_id:
                label_id[label] = current_id
                current_id += 1
            id_ = label_id[label]
            # print('Label ID', label_id)

            pil_image = Image.open(path).convert("L")  ##Open image using pillow and convert to grayscale
            size= (550,550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_arr = np.array(final_image, "uint8") ##Convert image to numpy array
            # print(image_arr)
            face = face_cascade.detectMultiScale(image_arr, scaleFactor=1.05, minNeighbors=5)

            for (x, y, w, h) in face:
                roi = image_arr[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

# print('x train', x_train)
# print('y labels', y_labels)

with open("labels.pickle", "wb") as f:
    pickle.dump(label_id, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
print("Done Training")