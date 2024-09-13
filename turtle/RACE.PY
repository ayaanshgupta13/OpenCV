import turtle
import time
import random

WIDTH,HEIGHT = 500,500

COLORS=['blue','red','orange','cyan','purple','brown','pink','black','green' ]

def get_number_of_racer():
    racers = 0
    while True:
        racers= input('Enter the number of racers (2-10): ')
        if racers.isdigit():
            racers=int(racers)
        else:
            print('input is not numeric.......try again')
            continue
        if 2<=racers<=10:
            create_turtle(COLORS)
        else:
            print('number not in range')


def create_turtle(color):
    turtles=[]
    spacingx= WIDTH//(len(colors)+1)
    for i , color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('turtle racing')

time.sleep(20)

init_turtle()
racers = get_number_of_racer()


racer = turtle.Turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]