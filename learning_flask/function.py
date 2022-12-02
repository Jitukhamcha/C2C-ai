import cv2

def myfunc(image,size):
    image=cv2.resize(image,(size,size))
    return image