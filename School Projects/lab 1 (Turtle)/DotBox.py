import turtle
s=turtle.Screen()
t=turtle.Turtle()

#offset
t.penup()
t.left(90)
t.forward(100)
t.left(90)
#drawbox
t.pendown()
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
#first dot
t.penup()
t.dot(20,'green')
#to bottomLeft
t.left(90)
t.forward(200)
t.dot(20,'yellow')
#to bottomRight
t.left(90)
t.forward(200)
t.dot(20,'red')
#to topLeft
t.left(90)
t.forward(200)
t.dot(20,'blue')

t.hideturtle()
