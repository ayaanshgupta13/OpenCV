import cv2

img = cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')
h,w , c = img.shape
center= 5,5
e=(w,h) 

center1= w//2,h//2
radius=h//2
color=(255,0,0)
img = cv2.rectangle(img,center,e,(0,255,255),-1)

img = cv2.circle(img,center1,radius,color,-1)

cv2.imshow('shape',img)
cv2.waitKey(0)