import cv2
img=cv2.imread('opencv/images/lambo.png')
h,w,c = img.shape
Start_point=(w,0)
endpoint=(0,h)
line_color = (0,255,0)
thickness=5

img = cv2.line(img,Start_point,endpoint,line_color,thickness)
cv2.imshow('og',img)
cv2.waitKey(0)