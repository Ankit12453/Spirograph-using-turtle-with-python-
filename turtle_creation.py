import turtle
import time

obj=turtle.Turtle()
obj.speed(0.2)
obj.penup()
obj.goto(0,120)
obj.pendown()

window = turtle.Screen()
window.colormode(255)

r=100
g=65
b=25

time.sleep(2)

for i in range(18):
    obj.pencolor((r,g,b))
    for j in range(36):
        obj.forward(100)
        obj.right(90)
        obj.forward(90)
        obj.right(100)
        obj.forward(101.12)
    obj.penup()
    obj.forward(45)
    obj.right(20)
    obj.pendown()

    r=r+8
    g=g+4
        

turtle.done()
