import cv2

img=cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')
h , w ,c = img.shape
print(h, w)
s_point = (0,h//2)
e_point = (w,h//2)
line_color = (0,255,0)
thickness=5

img = cv2.arrowedLine(img,s_point,e_point,line_color,thickness)

_point = (w//2,0)
de_point = (w//2,h)
dline_color = (0,255,0)
dthickness=5

img = cv2.arrowedLine(img,_point,de_point,dline_color,dthickness)
cv2.imshow('og',img)
cv2.waitKey(0)