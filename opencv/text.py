import cv2

img=cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')

font = cv2.FONT_HERSHEY_TRIPLEX
org = (200,200)
fontscale = 1
color = (255,0,0)


img = cv2.putText(img,'HELLO',org,font,fontscale,color,2)

cv2.imshow('og',img)
cv2.waitKey(0)