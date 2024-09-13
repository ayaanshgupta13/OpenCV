from tkinter import *
import sqlite3
import os 
from tkinter import messagebox
import cv2

root = Tk()
root.geometry('400x400')
root.title('CAMERA')
root.config(bg='#FFF8DC')

def cam():
    video_capture = cv2.VideoCapture(0)
    while video_capture.isOpened():
        x,frame = video_capture.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',gray)
        shutter = Button(root,text= ' ').pack()

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    video_capture.release()
camimg = PhotoImage(file='CAMERA/images/camera.png')
camera_button = Button(root,image=camimg,bg='#FFF8DC',command=lambda:cam()).grid(row=0,column=0)
cam_lbl = Label(root, text = 'camera', fg = 'black', bg = '#FFF8DC',font=('poppins',15)).grid(row=1,column=0)

root.mainloop()