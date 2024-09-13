from tkinter import*

import random
from tkinter import messagebox


root = Tk()

root.geometry("280x300")
root.title("*Roll The Dice*")

dice1=PhotoImage(file='scratch/images/dice-1.png')
dice2=PhotoImage(file='scratch/images/dice-2.png')
dice3=PhotoImage(file='scratch/images/dice-3.png')
dice4=PhotoImage(file='scratch/images/dice-4.png')
dice5=PhotoImage(file='scratch/images/dice-5.png')
dice6=PhotoImage(file='scratch/images/dice-6.png')
guess=StringVar()


score =0
def roll():
    global score
    print(guess.get())
    if guess.get() == '':
        responselbl['text']='please enter a number between 2-12'
    elif  guess.get().isalpha():
        responselbl['text']='please enter a number between 2-12'
    else:
        n=int(guess.get())
        if n < 2 or n > 12:
            responselbl['text']='please enter a number between 2-12'
        else:
            n1=random.randint(1,6)
            n2=random.randint(1,6)
            print(n1,n2)
            print('scratch/images/dice-'+str(n1)+".png")
            dice1=PhotoImage(file="scratch/images/dice-"+str(n1)+".png")
            dice2=PhotoImage(file="scratch/images/dice-"+str(n2)+".png")
            dice1lbl.config(image=dice1)
            dice2lbl.config(image=dice2)
        
            if n1+n2 == n:
                print('correct')
                r=messagebox.askyesno('','corect answer!!!!! ,do you wish to replay')
                score=+1
                scorelbl['text']="score - " + str(score)
                print(score)

            else:
                print('wrong')
                r=messagebox.askyesno('','wrong answer!!!!! ,do you wish to replay')
                responselbl['text']=''
                score+=-1
                scorelbl['text']="score -  " + str(score)
                print(score)

            if r:
                guess.set('')
            root.mainloop()


score=0
scorelbl=Label(root,text="score - " + str(score))
dice1lbl = Label(root, image=dice1)
dice2lbl = Label(root, image=dice2)
guesstxt=Entry(root,textvariable=guess,font=('arial',15) )
btn=Button(root,text='roll the dice',command=lambda:roll())
responselbl=Label(root,text='')

dice1lbl.grid(row=0, column=0)
dice2lbl.grid(row=0, column=1)
btn.grid(row=3,columnspan=2)
guesstxt.grid(row=1,columnspan=2)
responselbl.grid(row=4,columnspan=2)
scorelbl.grid()
root.mainloop()