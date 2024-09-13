from tkinter import *






def bills():
    global show_lable
    root = Tk()
    root.geometry('400x300')
    root.title('bills')
    root.config(bg='cyan')

    show_lable=Label(root,text='',bg="cyan")
    f = open("bills.txt", "r")
    cf=f.read()
    show_lable['text'] = cf

    root.mainloop()

def clearbills():
    f = open("bills.txt", "w")
    f.write('')
    show_lable['text'] = ' '