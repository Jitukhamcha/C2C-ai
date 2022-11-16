import cv2
import dlib
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt

#face detector and landmarks
face_detecter=dlib.get_frontal_face_detector()
face_landmark=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

mouth_start,mouth_end=face_utils.FACIAL_LANDMARKS_IDXS['mouth']
nose_start,nose_end=face_utils.FACIAL_LANDMARKS_IDXS['nose']
print(nose_start)
lefteye_start ,lefteye_end = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
righteye_start ,righteye_end = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

print(mouth_start)
#Read pictures
glassess=cv2.imread('glasses.png')
#glasses_array=np.array(glassess)
moustache=cv2.imread('moustache.png')
plt.imshow(glassess)
#for landmarks points
landmarks_points=[]
alpha=0.3
foreground=np.ones((100,100,3),dtype='int8')*255
cap=cv2.VideoCapture(0)

ret,img=cv2.threshold(glassess,1,255,cv2.THRESH_BINARY)
while True:
    ret,frame=cap.read()
    
    #setting frame size
    frame=cv2.resize(frame,(1280,720))
    
    #for computation handling
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detecter(gray,0)
    
    #For Displaying rectangle
    for face in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
        
        #Drawing Rectangle
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3) 
        
        #Getting Landmarks
        landmarks=face_landmark(frame,face)
        for i in range(68):
            x=landmarks.part(i).x
            y=landmarks.part(i).y
            
            #landmarks_points
            landmarks_points.append([x,y])
             
            #Drawing Using CV2 Circle
            frame=cv2.circle(frame,(x,y),1,(255,255,0),1)
        
        #area for moustache
        shape=face_landmark(gray,face)
        shape=face_utils.shape_to_np(shape)
        #for nose and mouth
        nose=shape[nose_start:nose_end]
        mouth=shape[mouth_start:mouth_end]
        
        left=mouth[0][0]
        right=mouth[6][0]
        up=nose[6][1]
        down=mouth[4][1]
        
        frame=cv2.rectangle(frame,(left,up),(right,down),(255,255,255),1)
        
        #for eyes
        nosestart,noseend = face_utils.FACIAL_LANDMARKS_IDXS['nose']
        mouthstart,mouthend = face_utils.FACIAL_LANDMARKS_IDXS['mouth']
        lefteyestart ,lefteyeend = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
        righteyestart ,righteyeend = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
        lefteyebrowstart,lefteyebrowend = face_utils.FACIAL_LANDMARKS_IDXS['left_eyebrow']
        righteyebrowstart,righteyebrowend = face_utils.FACIAL_LANDMARKS_IDXS['right_eyebrow']
        
        

        lefteye = shape[lefteyestart:lefteyeend]
        righteye = shape[righteyestart:righteyeend]
        nose = shape[nosestart:noseend]
        mouth = shape[mouthstart:mouthend]
        lefteyebrow = shape[lefteyebrowstart:lefteyebrowend]
        righteyebrow = shape[righteyebrowstart:righteyebrowend]


        #for glasses
        left1 = lefteyebrow[4][0]
        right1 = righteyebrow[0][0]
        up1 = nose[0][1]
        down1 = nose[2][1]

        dist_x1 = left1-right1
        dist_y1 = down1-up1
        print(dist_x1,dist_y1)

        
        #reading and resizing
        glass=cv2.imread('glasses.jpg')
        glass=cv2.resize(glass,(dist_x1,dist_y1))
        
        #setting static frame
        roi=frame[up1:down1,right1:left1]
        
        #converting to gray scale
        img2gray=cv2.cvtColor(glass,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('img2gray',img2gray)
        
        #masking so that the background is all black
        _,mask=cv2.threshold(img2gray,50,255,cv2.THRESH_BINARY)
        #cv2.imshow('mask',mask)
        
        #inversing mask so that subject is all black
        mask_inv=cv2.bitwise_not(mask)
        #cv2.imshow('inv_mask',mask_inv)
        
        #this ensures only colored glass is read
        frame_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
        
        #this now ensures background to go
        glass_fg=cv2.bitwise_and(glass,glass,mask=mask)
        
        
        roi=cv2.add(frame_bg,glass_fg)
        
        
        roi=cv2.add(frame_bg,glass_fg)
        
        frame[up1:down1,right1:left1]=roi
            
        #frame = cv2.rectangle(frame,(left1,up1),(right1,down1),(255,255,0), 2)
        #goggles = cv2.resize(roi,(dist_x1,dist_y1))
        #frame[up1:down1,right1:left1] = goggles
        
          
            
    #showing frames or video
    if ret:
        #cv2.imshow('Gray',gray)
        cv2.imshow('Original',frame)    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()