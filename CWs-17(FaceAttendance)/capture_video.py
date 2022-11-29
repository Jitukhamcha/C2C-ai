import cv2
import os
import time
import argparse
from dnn_face_detection import detect_face

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--name',  type=str,
                    help='Name')
args = parser.parse_args()


cap = cv2.VideoCapture(0)
_,frame = cap.read()
fh, fw,_ = frame.shape
fps = cap.get(cv2.CAP_PROP_FPS)

destination_path = os.path.join("dataset/video",args.name)
if not os.path.isdir(destination_path): 
    os.mkdir(destination_path)

out = cv2.VideoWriter(f"{destination_path}/{args.name}.avi",cv2.VideoWriter_fourcc(*'mp4v'),fps,(fw,fh))
start = time.time()
while cap.isOpened() :
    ret, frame = cap.read()   
    frame = cv2.flip(frame,1)
    faces = detect_face(frame)
    for bbounding_box in faces:
        x = int(bbounding_box[0])
        y = int(bbounding_box[1])
        x2 = int(bbounding_box[2])
        y2 = int(bbounding_box[3])
        # print(x,y,x2,y2)
        cv2.rectangle(frame, (x,y),(x2,y2),(255,0,0),1)
    
    count_time = int((time.time() - start))

    cv2.putText(frame, str(count_time),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,25,24))
    out.write(frame)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") or count_time >= 10:
        break



