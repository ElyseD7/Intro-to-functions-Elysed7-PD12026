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

t.speed(200)

def square(x):
    for i in range(4):
        t.forward(x)
        t.right(90)
#square(200)

# for i in range(60):
#     square(50)
#     t.right(5)

# def doublesquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length)
#         length = length * 2
# doublesquares(5) 
# turtle.done()

# def addsquare(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length)
#         length += 5
# addsquare(4) 

# def specsquare(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length) 
#         length += 5
#         t.right(5)
# specsquare(60)


# for i in range(50):
#     length = 25
#     square(length)
#     t.right(5)

def star(x):
    for i in range(5):
        t.forward(x)
        t.left(144)
star(1)

def specstar(iRange):
    length = 25
    for i in range(iRange):
        star(length) 
        length += 5
        t.right(5)
specstar(60)