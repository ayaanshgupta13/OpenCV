import cv2

img=cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')
h,w , c = img.shape
center= 5,5
e=(w,h) 

img = cv2.rectangle(img,center,e,(255,0,0),-1)

cv2.imshow('og',img)
cv2.waitKey(0)