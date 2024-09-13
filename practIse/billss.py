from tkinter import *
from tkinter import messagebox
import bills_show

def submit_button():
    add()

def show_button():
    bills_show.bills()

    # f = open("bills.txt", "r")
    # cf=f.read()
    # show_lable['text'] = cf

def clear_button():
    
    bills_show.clearbills()

root = Tk()
root.geometry('400x300')
root.title('bills')
root.config(bg='cyan')
userans=StringVar()
userans2=StringVar()
l1=Label(root,text='enter the seller name👇',font=("popins",20),bg="cyan")
x1 = Entry(root,text='',width=30,font=('popins',12),textvariable=userans)
l2=Label(root,text='enter the bill amount👇',font=("popins",20),bg="cyan")
y1 = Entry(root,text='',width=30,font=('popins',12),textvariable=userans2)
submit=Button(root,text='SUBMIT',width=20,height=1,command=lambda:submit_button())
show=Button(root,text='SHOW',width=20,height=1,command=lambda:show_button())
clear=Button(root,text='CLEAR ALL BILLS',width=20,height=1,command=lambda:clear_button())

def add():  
    x=userans.get()
    y=userans2.get()
    f = open("bills.txt", "a")
    f.write(format(x)  + ': ' + format(y) + ",  ")
    f.close()

    f = open("bills.txt", "r")
    f.close()
    
l1.pack()
x1.pack()
l2.pack()
y1.pack()
submit.pack()
show.pack()
clear.pack()
root.mainloop()