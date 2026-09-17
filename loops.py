# #loops programming

# for i in range(3):
#     print(i)

# for i in range(4):
#     t.forward(100)
#     t.left(90)
# turtle.done

import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
    
# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
# square(100,90)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)

turtle.done()