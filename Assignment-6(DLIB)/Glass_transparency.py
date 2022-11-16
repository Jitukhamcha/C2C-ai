import cv2
import numpy as np
from imutils import resize
from PIL import Image
cap = cv2.VideoCapture(0)
  
while(True):
      
    ret, frame = cap.read()
    frame=cv2.flip(frame,180)
    frame=cv2.resize(frame,(1280,720))
    
    #reading and resizing
    glass=cv2.imread('glass.jpg')
    glass=cv2.resize(glass,(200,200))
    
    #setting static frame   
    roi=frame[100:300,200:400]
    
    #converting to gray scale
    img2gray=cv2.cvtColor(glass,cv2.COLOR_BGR2GRAY)
    cv2.imshow('1 img2gray',img2gray)
    
    #masking so that the background is all black
    _,mask=cv2.threshold(img2gray,50,255,cv2.THRESH_BINARY)
    cv2.imshow('2 mask',mask)
    
    #inversing mask so that subject is all black
    mask_inv=cv2.bitwise_not(mask)
    cv2.imshow('3 inv_mask',mask_inv)
    
    #this ensures only colored glass is read
    frame_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
    
    #this now ensures background to go
    glass_fg=cv2.bitwise_and(glass,glass,mask=mask)
    cv2.imshow('4 glass_fg',glass_fg)
    
    roi=cv2.add(frame_bg,glass_fg)
    cv2.imshow('5 roi',roi)
    
    roi=cv2.add(frame_bg,glass_fg)
    
    frame[100:300,200:400,:]=roi
    
    
    cv2.imshow('video original', frame)
    
    if cv2.waitKey(1) == 27:
        break
  
cap.release()
cv2.destroyAllWindows()