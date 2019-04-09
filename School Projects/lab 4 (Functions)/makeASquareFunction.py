#create a function that draws a square with its center at (x,y)
import turtle
s = turtle.Screen()
t = turtle.Turtle()

def drawSquare(xLoc, yLoc, size, color, aTurtle):
    aTurtle.speed(0)
    aTurtle.pencolor(color)
    aTurtle.penup(); aTurtle.goto(xLoc,yLoc); aTurtle.pendown()
    aTurtle.forward(size/2); aTurtle.left(90); aTurtle.forward(size/2)
    aTurtle.fillcolor(color); aTurtle.begin_fill()
    for i in range(4):
        aTurtle.left(90)
        aTurtle.forward(size)
    aTurtle.end_fill()


drawSquare(-150, 20, 50, 'green', t)
drawSquare(20, 20, 100, 'purple', t)
drawSquare(100, -30, 80, 'cyan', t)
drawSquare(-100, -100, 150, 'magenta', t)
drawSquare(300, 200, 100, 'yellow', t)
t.penup()
t.goto(0, 0)
t.pendown()
t.dot(10, 'red')
