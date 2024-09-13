import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('opencv/lamborgini-gdd8223bd8_640.jpg')

half = cv2.resize(image,(0,0),fx=0.1,fy=0.1)
double = cv2.resize(image,(0,0),fx=2,fy=2)

titles=['orignals','half','origignal']
images = [image,half,image]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])

plt.show()