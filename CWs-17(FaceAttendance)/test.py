import cv2
import numpy as np
from dnn_face_detection import detect_face
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
from keras_facenet import FaceNet
# model = tf.saved_model.load('facenet.h5')
from keras_facenet import FaceNet

embeder = FaceNet()
facenet_model = embeder.model

model = Sequential()
facenet_model.trainable = False
model.add(facenet_model)

model.add(Flatten())
model.add(Dense(8, activation="softmax"))



model.load_weights("C:/Users/Ghost/Desktop/AIML/c2c-ai/CWs-17(FaceAttendance)/weights.h5")
model.summary()



cap = cv2.VideoCapture(0)

classes = ['badal',
 'bibek',
 'mukesh',
 'nasla',
 'prapti',
 'sujen',
 'swastika']

while cap.isOpened() :
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame,1)
        faces = detect_face(frame)
        if len (faces) > 0:
            for bbounding_box in faces:
                x = int(bbounding_box[0])
                y = int(bbounding_box[1])
                x2 = int(bbounding_box[2])
                y2 = int(bbounding_box[3])
                crop_face = frame[y:y2, x:x2]
                crop_face = cv2.resize(crop_face, (160,160))
                
                result = model.predict(np.expand_dims(crop_face/255, axis=0))
                
                accuracy = result[0][np.argmax(result)]
                print(accuracy)

                label = classes[np.argmax(result)]
                cv2.putText(frame, label,(x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(255,15,220),1)
                cv2.rectangle(frame, (x,y),(x2,y2),(255,0,0),1)

                cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()
