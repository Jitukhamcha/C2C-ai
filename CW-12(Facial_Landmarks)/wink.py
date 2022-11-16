import cv2
import dlib
from imutils import face_utils
from scipy.spatial import distance as dist

face_detector = dlib.get_frontal_face_detector()
face_landmark = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

THRESHOLD = 0.15



lefteyestart ,lefteyeend = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
righteyestart ,righteyeend = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']


cap = cv2.VideoCapture(0)

def eye_ratio(eye):
    A = dist.euclidean(eye[1],eye[5])
    B = dist.euclidean(eye[2],eye[4])
    C = dist.euclidean(eye[0],eye[3])

    e_ratio = (A + B )/ (2*C)
    return e_ratio




while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,180)
    frame = cv2.resize(frame,(1280,720))
    if ret:
        #frame = cv2.rotate(frame, cv2.ROTATE_180)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray, 0)
        print(faces)

        for (i, rect) in enumerate(faces):
            (x,y,w,h) = face_utils.rect_to_bb(rect)

            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 2)
            frame = cv2.putText(frame, f"face{i}", (x,y-10), 1,2,(0,255,255),2)

            shape = face_landmark(gray,rect)
            shape = face_utils.shape_to_np(shape)

            for (x,y) in shape:
                frame = cv2.circle(frame,(x,y),1,(255,255,0),1)

            lefteye = shape[lefteyestart:lefteyeend]
            righteye = shape[righteyestart:righteyeend]

            lefteyeratio = eye_ratio(lefteye)
            righteyeratio = eye_ratio(righteye)

            #if (((lefteyeratio < THRESHOLD) and ( righteyeratio > THRESHOLD)) or ((righteyeratio  < THRESHOLD) and ( lefteyeratio > THRESHOLD))):
            if(lefteyeratio<THRESHOLD):
                if(righteyeratio>THRESHOLD):
                    frame = cv2.putText(frame, "Wink Detected!!!!!", (10,25), 1,2,(0,255,255),2)
            elif(righteyeratio<THRESHOLD):
                if(lefteyeratio>THRESHOLD):
                    frame = cv2.putText(frame, "Wink Detected!!!!!", (10,25), 1,2,(0,255,255),2)
                
                    



    if ret:
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()