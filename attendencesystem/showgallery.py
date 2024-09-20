from tkinter import *
import sqlite3
from tkinter import messagebox
import os
class DisplayGallery():
    def __init__(self):
        root = Tk()
        root.title("Gallery")
        root.geometry('500x500')
        root.config(bg="#333")
        path = "attendancesystem/student-images"
        folders = os.listdir(path)
        print(folders)
        r = 0
        col = 0
        for folder in folders:
            folderpath = path+"/"+folder
            print(folderpath) 
            files = os.listdir(folderpath)
            for file in files:
               print(file)
               break
            img = PhotoImage(file=folderpath+"/"+file)
            print(img)
            Label(root, text=folder, bg="#333", fg="white", font=("poppins",12)).grid(row=r, column=col, padx=10)
            col+=1
            if col > 2:
             col = 0
             r+=1
        

        root.mainloop()