import cv2

face_C=cv2.CascadeClassifier('opencv/haarcascade_frontalface_default.xml')
image = cv2.imread('opencv/collage-of-portraits-and-faces-of-smiling-multiracial-group-of-various-diverse-people-for-profile-picture-on-colorful-background-diversity-concept-generative-ai-photo.jpg')

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_C.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),((x+w),(y+h)),(0,0,255),3)

cv2.imshow('video',image)
cv2.waitKey(0)