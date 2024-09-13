import cv2

i = cv2.imread("opencv/lamborgini-gdd8223bd8_640.jpg", cv2.IMREAD_COLOR)
cv2.imshow('car',i)
cv2.waitKey(0)