import cv2
import os

image_path=r'opencv/lamborgini-gdd8223bd8_640.jpg'

directory =r'C:/Users/neera/OneDrive\Desktop/python/opencv/images'

img=cv2.imread(image_path)

os.chdir(directory)
print('before saving our file to folder')
print(os.listdir(directory))

filename='car.jpg'
cv2.imwrite(filename,img)