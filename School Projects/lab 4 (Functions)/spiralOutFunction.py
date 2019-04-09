#create a function that draws a square spiral
import turtle
s = turtle.Screen()
t = turtle.Turtle()
u = turtle.Turtle()
v = turtle.Turtle()
golden = 1.618
t.speed(0);u.speed(0);v.speed(0)

def spiralSquare(numSteps,color,aTurtle):
    aTurtle.pendown()
    aTurtle.color(color); aTurtle.pencolor(color)
    scaleFactor = 10
    for i in range(1,numSteps + 1):
        aTurtle.forward(i*scaleFactor*golden)
        aTurtle.right(90)
    aTurtle.penup()

def graphicHallway():
    spiralSquare(26,'red',t)
    u.penup(); u.goto(3,3)
    spiralSquare(26,'green',u)
    v.penup();v.goto(6,6)
    spiralSquare(26,'blue',v)

def continuousSpiral():
    spiralSquare(26,'red',t)
    spiralSquare(26,'green',t)

def spiralFlower():
    for i in range(8):
        spiralSquare(5,'purple',t)
        t.right(45)


