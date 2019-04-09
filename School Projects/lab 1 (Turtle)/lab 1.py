import turtle
import math
s=turtle.Screen()
t=turtle.Turtle()
#Functions
def DrawBox(thickness,color,height,width):
    t.pendown()
    t.pensize(thickness)
    t.pencolor(color)
    t.setheading(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.setheading(0)
def Down(d):
    t.setheading(-90)
    t.forward(d)
def Up(u):
    t.setheading(90)
    t.forward(u)
def Right(r):
    t.setheading(0)
    t.forward(r)
def Left(l):
    t.setheading(180)
    t.forward(l)
#OrientRoof
t.penup()
Up(100)
t.left(45)
t.pensize(5)
t.pencolor('brown')
#drawRoof
t.pendown()
t.left(90)
t.forward(200)
t.backward(200)
t.left(90)
t.forward(200)
Left(math.sqrt(80000))
#drawHouseBody
DrawBox(5,'blue',200,math.sqrt(80000))
#OrientGarage
t.penup()
Right(math.sqrt(80000))
Down(25)
#DrawGarage
DrawBox(5,'blue',175,150)
#OrientGDoor
t.penup()
Right(30)
Down(45)
#DrawGDoor
DrawBox(5,'grey',130,90)
#OrientDoor
t.penup()
Down(50)#Door is height 80
Left(180)
#DrawDoor
DrawBox(5,'brown',80,50)
#OrientWindow
t.penup()
Up(60)
Left(90)
#DrawWindow
DrawBox(2,'black',60,60)
#OrientWindow2


