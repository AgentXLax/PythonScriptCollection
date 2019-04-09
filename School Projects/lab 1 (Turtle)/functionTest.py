import turtle
import math
s=turtle.Screen()
t=turtle.Turtle()

def DrawBox(color,height,width):
    t.pencolor(color)
    t.setheading(0)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)

DrawBox(color='blue',height=50,width=50)
