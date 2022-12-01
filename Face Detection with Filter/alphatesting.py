import cv2
import numpy as np
from imutils import resize
  
cap = cv2.VideoCapture(0)
  
while(True):
      
    ret, frame = cap.read()
    frame=cv2.flip(frame,180)
    frame=cv2.resize(frame,(1280,720))
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # Import the image
    file_name = "gfg_black.png"
  
    # Read the image
    src = cv2.imread(file_name, 1)
    
    # Convert image to image gray
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    # Applying thresholding technique
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    
    # Using cv2.split() to split channels 
    # of coloured image
    b, g, r = cv2.split(src)
    
    # Making list of Red, Green, Blue
    # Channels and alpha
    rgba = [b, g, r, alpha]
    
    # Using cv2.merge() to merge rgba
    # into a coloured/multi-channeled image
    dst = cv2.merge(rgba, 4)
    
    
        
    frame[100:420, 100:420 ] = dst
    
   # glassess=cv2.resize(glassess,(640,480))
    
    #frame[0:20,0:20]=glassess_cut
    
    
    
    
    
    #cv2.imshow('gh',glassess_cut)
    cv2.imshow('video original', frame)
    
    if cv2.waitKey(1) == 27:
        break
  
cap.release()
cv2.destroyAllWindows()