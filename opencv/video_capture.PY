import cv2

# face_C=cv2.CascadeClassifier('opencv/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
    x,frame = video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('video',gray)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video_capture.release()