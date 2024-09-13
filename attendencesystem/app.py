from tkinter import *
from addstudent import *
from showgallery import *

root = Tk()
root.geometry('400x400')
root.title('attendance system')
root.config(bg='#333')

def getstudent():
    Student()

def showstudent():
    Displaygallery()


addimg = PhotoImage(file='attendencesystem/app-images/add-user.png')
addbtn = Button(root,image=addimg,bg='#333',command=lambda:getstudent()).grid(row=0,column=0)
Label(root,text='Add student',bg='#333',fg='cyan').grid(row=1,column=0)


galimg = PhotoImage(file='attendencesystem/app-images/picture.png')
galbtn = Button(root,image=galimg,bg='#333',command=lambda:showstudent()).grid(row=0,column=1)
Label(root,text='Show Students',bg='#333',fg='cyan').grid(row=1,column=1)



root.mainloop()