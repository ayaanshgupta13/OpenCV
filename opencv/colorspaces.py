import cv2

image=cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')
print(image)

B, R, G, = cv2.split(image)

cv2.imshow('orignal',image)
cv2.waitKey(0)

cv2.imshow('blue',B)
cv2.waitKey(0)

cv2.imshow('green',G)
cv2.waitKey(0)

cv2.imshow('red',R)
cv2.waitKey(0)