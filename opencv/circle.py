import cv2

img=cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')
h,w , c = img.shape
center= w//2,h//2
radius=h//2
color=(0,255,0)

img = cv2.circle(img,center,radius,radius,-1)

cv2.imshow('og',img)
cv2.waitKey(0)