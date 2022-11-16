#importing libraryies
import cv2
import dlib
from imutils import face_utils
from scipy.spatial import distance as dist

#initialization of facial detector and facial landmarks
face_detector = dlib.get_frontal_face_detector()
face_landmark= dlib.shape_predictor('/home/sujen/projects/c2c-ai/assignment-5/shape_predictor_68_face_landmarks.dat')

#using facial landmark indexes to find start and end points
nosestart,noseend = face_utils.FACIAL_LANDMARKS_IDXS['nose']
mouthstart,mouthend = face_utils.FACIAL_LANDMARKS_IDXS['mouth']
lefteyestart ,lefteyeend = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
righteyestart ,righteyeend = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
lefteyebrowstart,lefteyebrowend = face_utils.FACIAL_LANDMARKS_IDXS['left_eyebrow']
righteyebrowstart,righteyebrowend = face_utils.FACIAL_LANDMARKS_IDXS['right_eyebrow']
jawstart,jawend = face_utils.FACIAL_LANDMARKS_IDXS['jaw']

#capturing video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    if ret:
        #changing captured video to grayscale for faster calculations
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray, 0)
        print(faces)
            
        for (i, rect) in enumerate(faces):
            
            (x,y,w,h) = face_utils.rect_to_bb(rect)
            
            #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 2)
            #frame = cv2.putText(frame, "face", (x,y-10), 1,2,(0,255,255),2)

            shape = face_landmark(gray,rect)
            shape = face_utils.shape_to_np(shape)

            '''for (x,y) in shape:
                frame = cv2.circle(frame,(x,y),3,(255,255,0),2)'''

            #assigning vaues to facial landmarks
            lefteye = shape[lefteyestart:lefteyeend]
            righteye = shape[righteyestart:righteyeend]
            nose = shape[nosestart:noseend]
            mouth = shape[mouthstart:mouthend]
            lefteyebrow = shape[lefteyebrowstart:lefteyebrowend]
            righteyebrow = shape[righteyebrowstart:righteyebrowend]
            jaw = shape[jawstart:jawend]



            #for glasses

            #creating new bb for glasses
            left1 = lefteyebrow[4][0]
            right1 = righteyebrow[0][0]
            up1 = righteyebrow[2][1]
            down1 = nose[4][1]

            #width = dist_x1 and height = dist_y1
            dist_x1 = left1-right1
            dist_y1 = down1-up1
            print(dist_x1,dist_y1)

            #frame = cv2.rectangle(frame,(left1,up1),(right1,down1),(255,255,255), 2)
            
            #importing glasses image
            glass = cv2.imread('glasses.jpg')

            #resizing to fit bb of glasses (+50 is done for scaling)
            glass=cv2.resize(glass,(dist_x1+50,dist_y1+50))

            #creating region of interest 
            roi=frame[up1-25:down1+25,right1-25:left1+25]

            #converting glassses image to gray
            img2gray=cv2.cvtColor(glass,cv2.COLOR_BGR2GRAY)
            #cv2.imshow('img2gray',img2gray)

            #using binary thresholding as mask
            _,mask=cv2.threshold(img2gray,0,255,cv2.THRESH_BINARY)
            #cv2.imshow('mask',mask)

            #creating mask inverse mask     
            mask_inv=cv2.bitwise_not(mask)
            #cv2.imshow('inv_mask',mask_inv)

            frame_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

            mustache_fg=cv2.bitwise_and(glass,glass,mask=mask)

            roi=cv2.add(frame_bg,mustache_fg)

            roi=cv2.add(frame_bg,mustache_fg)

            #adding glasses to frame
            frame[up1-25:down1+25,right1-25:left1+25]=roi

            #for mustache

            #creating new bb for mustache
            right = mouth[0][0]
            left = mouth[6][0]
            up = nose[6][1]
            down = mouth[4][1]

            #width = dist_x, height= dist_y
            dist_x = left-right
            dist_y = down-up
            print(dist_x,dist_y)

            #frame = cv2.rectangle(frame,(left,up),(right,down),(255,255,255), 2)

            #reading from mustache image
            mustache = cv2.imread('mustache.jpg')

            mustache=cv2.resize(mustache,(dist_x+50,dist_y+50))

            roi=frame[up-25:down+25,right-25:left+25]

            img2gray=cv2.cvtColor(mustache,cv2.COLOR_BGR2GRAY)
            #cv2.imshow('img2gray',img2gray)

            #usign threshold binary inverse  because the background of mustache img is white
            _,mask=cv2.threshold(img2gray,0,255,cv2.THRESH_BINARY_INV)
            #cv2.imshow('mask',mask)

            mask_inv=cv2.bitwise_not(mask)
            #cv2.imshow('inv_mask',mask_inv)

            frame_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
            #cv2.imshow("mustache",mustache)

            mustache_fg=cv2.bitwise_and(mustache,mustache,mask=mask)

            roi=cv2.add(frame_bg,mustache_fg)

            roi=cv2.add(frame_bg,mustache_fg)

            #adding mustache filter to frameq
            frame[up-25:down+25,right-25:left+25]=roi

        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()