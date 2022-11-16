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
jaw_start,jaw_end=face_utils.FACIAL_LANDMARKS_IDXS['jaw']
righteyebrow_start,righteyebrow_end = face_utils.FACIAL_LANDMARKS_IDXS['right_eyebrow']

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
    frame=cv2.flip(frame,180)
    #for computation handling
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detecter(gray,0)
    
    #For Displaying rectangle
    for face in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
            
        #Drawing Rectangle
        #frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3) 
            
        #Getting Landmarks
        landmarks=face_landmark(frame,face)
        for i in range(68):
            x=landmarks.part(i).x
            y=landmarks.part(i).y
                
            #landmarks_points
            landmarks_points.append([x,y])
                
            #Drawing Using CV2 Circle
            #frame=cv2.circle(frame,(x,y),1,(255,255,0),1)
            
        shape=face_landmark(gray,face)
        shape=face_utils.shape_to_np(shape)
        #for nose and mouth
        nose=shape[nose_start:nose_end]
        mouth=shape[mouth_start:mouth_end]
        
        #area to put moustache    
        right=mouth[0][0]-50
        left=mouth[6][0]+50
        up=nose[6][1]-50
        down=mouth[4][1]+50
        dist_x1_m=left-right
        dist_y1_m=down-up
        
        #Prevents Crashing    
        if left<=1280 and left>=0 and right>=0 and right<1280 and up<=720 and down<=720 and up>=0 and down>=0:
            #reading and resizing
            moustache=cv2.imread('moustache__resize.jpg')
            moustache=cv2.resize(moustache,(dist_x1_m,dist_y1_m))
                
            #setting Moustache frame   
            roi=frame[up:down,right:left]
                
            #converting to gray scale
            img2gray=cv2.cvtColor(moustache,cv2.COLOR_BGR2GRAY)
                
            #masking so that the background is all white # inverse because moustache is all black
            _,mask=cv2.threshold(img2gray,50,255,cv2.THRESH_BINARY_INV)
                
            #inversing mask so that subject is all white
            mask_inv=cv2.bitwise_not(mask)
                
            #this ensures only moustache  is read
            frame_bg_m=cv2.bitwise_and(roi,roi,mask=mask_inv)
                
            #this now ensures background to go
            moustache_fg=cv2.bitwise_and(moustache,moustache,mask=mask)
            
            #adds bg and fg    
            roi_m=cv2.add(frame_bg_m,moustache_fg)
                
            #adds to frame    
            roi_m=cv2.add(frame_bg_m,moustache_fg)
                
            frame[up:down,right:left]=roi_m
            
        #for eyes
        
        nose = shape[nose_start:nose_end]
        righteyebrow = shape[righteyebrow_start:righteyebrow_end]
        jaw=shape[jaw_start:jaw_end]

        #for glasses
        left1=jaw[16][0]+70
        right1=jaw[2][0]-70
        up1 = righteyebrow[2][1]-50
        down1 = nose[4][1]+50

        dist_x1 = left1-right1
        dist_y1 = down1-up1
            
        #Prevents Crashing
        if left1<=1280 and left1>=0 and right1>=0 and right1<1280 and up1<=720 and down1<=720 and up1>=0 and down1>=0:
            #reading and resizing
            glass=cv2.imread('glass.jpg')
            glass=cv2.resize(glass,(dist_x1,dist_y1))
                
            #setting Glass frame
            roi=frame[up1:down1,right1:left1]
                
            #converting to gray scale
            img2gray=cv2.cvtColor(glass,cv2.COLOR_BGR2GRAY)
            
            #masking so that the background is all black
            _,mask=cv2.threshold(img2gray,0,255,cv2.THRESH_BINARY)
            #cv2.imshow('mask',mask)
                
            #inversing mask so that subject is all black
            mask_inv=cv2.bitwise_not(mask)
                
            #this ensures only colored glass is read
            frame_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
                
            #this now ensures background to go
            glass_fg=cv2.bitwise_and(glass,glass,mask=mask)
                
            #adds bg and fg   
            roi=cv2.add(frame_bg,glass_fg)
            
            #adds to frame   
            frame[up1:down1,right1:left1]=roi
    
    #showing frames or video    
    if ret:
        #cv2.imshow('Gray',gray)
        cv2.imshow('Original',frame)    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()