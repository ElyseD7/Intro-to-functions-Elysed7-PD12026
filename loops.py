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

# sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
# square(100,90)

# t.speed(100)
# sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(60):
# #         t.forward(x)
# #         t.left(y+5)
# # square(100,90)

# def triangle(x,y):
#     for i in range(3):
#         t.forward(x)
#         t.left(y)
# triangle(100,120)
# turtle.done()

t.speed(100)

def square(x,y):
    for i in range(60):
        t.forward(x)
        t.right(y+5)
square(200,90)