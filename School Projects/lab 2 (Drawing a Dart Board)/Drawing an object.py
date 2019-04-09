#Construct a program that displays shapes in a variety of colors, based on the
#user's input.

import turtle
s = turtle.Screen()
t = turtle.Turtle()
#variables
colorList = ['black','yellow','cyan','magenta']
shapeList = ['truck','Truck','bird','Bird','flower','Flower']
shape = input('Enter a shape: truck, bird, or flower: ' )
color = input('What color would you like it? ' )

t.pensize(5)
#changing the color of the pen
if color in colorList :
    t.pencolor(color)
elif color in shapeList :
    print('not a color.')
else :
    print(str(color),'is the new black.')
    t.pencolor('black')
    color = 'black'

#Drawing the objects
if  shape == 'truck' or shape == 'Truck' :
    
    #Draw a Truck
    print('a truck')
    t.goto(30,30)
    t.goto(100,30)
    t.goto(100,-40)
    t.goto(0,-40)
    t.goto(0,0)
    t.penup()
    t.goto(20,-40)
    t.dot(40,color)
    t.goto(80,-40)
    t.dot(40,color)
    

elif shape == 'bird' or shape == 'Bird' :
    #Draw a Bird
    print('a bird')
    t.pendown()
    t.goto(-70,30)
    t.goto(0,0)
    t.goto(-70,-30)
    t.penup()
    t.goto(-120,-45)
    t.pendown()
    t.circle(50)
    

elif shape == 'flower' or shape == 'Flower' :
    #Draw a pretty rittle frower
    print('its a dandelion you dont know my life.')
    t.pendown()
    t.pensize(13)
    t.goto(0,-150)
    t.penup()
    t.goto(0,0)
    t.dot(60,color)

elif shape in colorList :
    print('not a shape.')

else :
    print('wrong move, f***boy.')
