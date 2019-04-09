#LAB 2: Bullseye
#Nathan Wisla
#AUCSC111

import turtle

s = turtle.Screen()
t = turtle.Turtle()
#Drawing the Bullseye:
t.speed(0); t.penup(); t.pencolor('brown'); t.goto(-100,100)
t.pendown(); t.goto(100,100); t.goto(100,-100); t.goto(-100,-100); t.goto(-100,100); t.penup()
t.goto(0,-50); t.pendown()
t.pencolor('blue'); t.fillcolor((.25,.8,1))
t.begin_fill(); t.circle(50); t.end_fill(); t.hideturtle()

#variables
print('You have one dart. Use it wisely.')
xCoord = float(input('Enter x-coordinate: ')) * 10
yCoord =  float(input('Enter y-coordinate: ')) * 10

#Placing the Dart
t.penup()
t.goto(xCoord,yCoord)
t.dot(5,'red')

#if condition within the constraints of the circle (x**2+y**2=50**2).
if xCoord**2 + yCoord**2 <= 50**2 :
    t.goto(-200,-200)
    t.write('Good job!')
#if condition inside the box (squares return positive values).
elif xCoord**2 <= 100**2 and yCoord**2 <= 100**2 :
    t.goto(-200,-200)
    t.write('At least you hit the board...')
#Outside the box.
else :
    t.goto(-200,-200)
    t.write('Are you even trying?')
