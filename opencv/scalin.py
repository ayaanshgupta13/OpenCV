import cv2
import matplotlib as plt

i = cv2.imread("opencv/lamborgini-gdd8223bd8_640.jpg", cv2.IMREAD_GRAYSCALE)

print(i.shape)
height , width = i.shape
print(height , width)
scale_double= 2
scale_half  = 1/2

h_h = float(height *scale_half )
h_w = float(width * scale_half)
# hsize= (h_h,h_w)
hsize = cv2.resize(i , (0,0),fx=h_h, fy=h_w)

d_h = int(height *scale_half )
d_w  = int(width * scale_half)
# dsize = (d_h,d_w)

cv2.imshow('OG',i)
cv2.imshow('Half',i)
# cv2.imshow(i)

cv2.waitKey(0)