'''
Created on Mar 15, 2020

@author: alexd
'''

from turtle import * 
from random import * 
from math import *
from time import *

#my turtle 
alex = Turtle() 
#so we dont see the turtle move (go really really fast)
alex.speed(0)
#hide the little turtle/triangle
alex.hideturtle()
#the screen itself 
screen = alex.screen 
# set up a screen with a width and height with start x and start y positions at 0,0
# 0, 0 would be the center of the screen (facing east or right)
screen.setup(width=1200, height=675, startx=0, starty=0)

#screen.tracer(0)

#HELPER FUNCTIONS
#drawing of a rectangle
def rectangleR(width, height, color, turtle1):
    turtle1.pendown()
#     turtle1.setheading(0)
    turtle1.color(color)
    turtle1.begin_fill()
    for i in range(2):
        turtle1.forward(width)
        turtle1.left(90)
        turtle1.forward(height)
        turtle1.left(90)

    turtle1.end_fill()
    turtle1.penup()
    return None

#drawing of a rectangle
def rectangleL(width, height, color, turtle1):
    turtle1.pendown()
#     turtle1.setheading(0)
    turtle1.color(color)
    turtle1.begin_fill()
    for i in range(2):
        turtle1.back(width)
        turtle1.right(90)
        turtle1.back(height)
        turtle1.right(90)

    turtle1.end_fill()
    turtle1.penup()
    return None

#equilateral triangle staring at midbase
def triangle(size, color, turtle1):
    turtle1.pendown()
#     turtle1.setheading(0)
    turtle1.color(color)
    turtle1.begin_fill()
    turtle1.forward(size/2)
    turtle1.left(120)
    turtle1.forward(size)
    turtle1.left(120)
    turtle1.forward(size)
    turtle1.left(120)
    turtle1.forward(size/2)
    turtle1.end_fill()
    turtle1.penup()
    return None

#drawing of the sun
def sunshine(turtle1):
    turtle1.fillcolor("Yellow")
    turtle1.pencolor("Yellow")
    turtle1.penup()
    turtle1.goto(-400,100)
    turtle1.setheading(0)
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.circle(100)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.goto(-539,(200-28.8675134595))
    turtle1.color("Yellow")
    turtle1.begin_fill()
    for i in range(12):
        turtle1.forward(278)
        turtle1.left(150)
    turtle1.end_fill()
    turtle1.penup()
    return None

#arms, legs, mouth, and eyes will all be color black
def draw_robot1(turtle1, x_val):
    #right shoe
    turtle1.goto(x_val,-(screen_height/4)+(60/sqrt(2))-90)
    turtle1.setheading(-45)
    rectangleR(60, 25, "black", turtle1)
    #right leg
    turtle1.goto(x_val+25*2/sqrt(2),-(screen_height/4)+(60/sqrt(2))-90)
    turtle1.setheading(45)
    rectangleR(100, 20, "purple", turtle1)
    #left arm (behind/before body) 
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    turtle1.setheading(225)
    rectangleR(15, 70, "red", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100+70/sqrt(2)-7.5*sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-70/sqrt(2)-7.5*sqrt(2)-90)
    turtle1.setheading(-45)
    rectangleR(12.5, 40, "red", turtle1)
    #body
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-90)
    turtle1.setheading(0)
    rectangleR(100, 170, "blue", turtle1)
    #neck
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+37.5,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    rectangleR(25, 30, "black", turtle1)
    #right arm
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    turtle1.setheading(135)
    rectangleL(15, 70, "red", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)-70/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-70/sqrt(2)-90)
    turtle1.left(90)
    rectangleR(12.5, 40, "red", turtle1)
    #left leg
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100-20/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-90)
    turtle1.setheading(-45)
    rectangleR(100, 20, "purple", turtle1)
    #left shoe
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100-20/sqrt(2)+125/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-125/sqrt(2)-90)
    turtle1.setheading(45)
    rectangleR(60, 25, "black", turtle1)
    #head
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200-90)
    turtle1.setheading(0)
    rectangleR(80, 60, "blue", turtle1)
    #eyes
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(10, 10, "white", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+3,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(5, 5, "black", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+30,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(10, 10, "white", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+30+3,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(5, 5, "black", turtle1)
    #mouth
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+20,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+20-90)
    turtle1.setheading(-95)
    rectangleR(10, 45, "black", turtle1)
    for i in range(5,45,5):
        turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+20+i*0.996194698092,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+20-i*0.087155742748-90)
        rectangleR(2, 2, "white", turtle1)
    
    
    return None


#arms, legs, mouth, and eyes will all be color black
def draw_robot2(turtle1, x_val):
    #right shoe
    turtle1.goto(x_val,-(screen_height/4)+(60/sqrt(2))-90)
    turtle1.setheading(-45)
    rectangleR(60, 25, "black", turtle1)
    #left leg
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100-20/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-90)
    turtle1.setheading(-45)
    rectangleR(100, 20, "purple", turtle1)
    #right arm
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    turtle1.setheading(135)
    rectangleL(15, 70, "red", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)-70/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-70/sqrt(2)-90)
    turtle1.left(90)
    rectangleR(12.5, 40, "red", turtle1)
    #body
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-90)
    turtle1.setheading(0)
    rectangleR(100, 170, "blue", turtle1)
    #right leg
    turtle1.goto(x_val+25*2/sqrt(2),-(screen_height/4)+(60/sqrt(2))-90)
    turtle1.setheading(45)
    rectangleR(100, 20, "purple", turtle1)
    #left arm (infront/after body) 
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    turtle1.setheading(225)
    rectangleR(15, 70, "red", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100+70/sqrt(2)-7.5*sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-70/sqrt(2)-7.5*sqrt(2)-90)
    turtle1.setheading(-45)
    rectangleR(12.5, 40, "red", turtle1)
    #neck
    turtle1.setheading(0)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+37.5,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    rectangleR(25, 30, "black", turtle1)
    #left shoe
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100-20/sqrt(2)+125/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-125/sqrt(2)-90)
    turtle1.setheading(45)
    rectangleR(60, 25, "black", turtle1)
    #head
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200-90)
    turtle1.setheading(0)
    rectangleR(80, 60, "blue", turtle1)
    #eyes
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(10, 10, "white", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+3,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(5, 5, "black", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+30,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(10, 10, "white", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+30+3,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(5, 5, "black", turtle1)
    #mouth
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+20,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+20-90)
    turtle1.setheading(-95)
    rectangleR(10, 45, "black", turtle1)
    for i in range(5,45,5):
        turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+20+i*0.996194698092,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+20-i*0.087155742748-90)
        rectangleR(2, 2, "white", turtle1)
    
    
    return None

def draw_robot3(turtle1, x_val):
    #right shoe
    turtle1.goto(x_val,-(screen_height/4)+(60/sqrt(2))-90)
    turtle1.setheading(-45)
    rectangleR(60, 25, "black", turtle1)
    #right leg
    turtle1.goto(x_val+25*2/sqrt(2),-(screen_height/4)+(60/sqrt(2))-90)
    turtle1.setheading(45)
    rectangleR(100, 20, "purple", turtle1)
    #left arm (behind/before body) 
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    turtle1.setheading(225)
    rectangleR(15, 70, "red", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100+70/sqrt(2)-7.5*sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-70/sqrt(2)-7.5*sqrt(2)-90)
    turtle1.setheading(-45)
    rectangleR(12.5, 40, "red", turtle1)
    #body
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-90)
    turtle1.setheading(0)
    rectangleR(100, 170, "blue", turtle1)
    #neck
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+37.5,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    rectangleR(25, 30, "black", turtle1)
    #right arm
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170-90)
    turtle1.setheading(135)
    rectangleR(70, 15, "red", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)-70/sqrt(2)+10,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+170+70/sqrt(2)-10.9-90)
    turtle1.left(215)
    rectangleL(12.5, 40, "red", turtle1)
    #left leg
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100-20/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-90)
    turtle1.setheading(-45)
    rectangleR(100, 20, "purple", turtle1)
    #left shoe
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+100-20/sqrt(2)+125/sqrt(2),-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))-125/sqrt(2)-90)
    turtle1.setheading(45)
    rectangleR(60, 25, "black", turtle1)
    #head
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200-90)
    turtle1.setheading(0)
    rectangleR(80, 60, "blue", turtle1)
    #eyes
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(10, 10, "white", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+3,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(5, 5, "black", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+30,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(10, 10, "white", turtle1)
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+22+30+3,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+40-90)
    rectangleR(5, 5, "black", turtle1)
    #mouth
    turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+20,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+20-90)
    turtle1.setheading(-95)
    rectangleR(10, 45, "black", turtle1)
    for i in range(5,45,5):
        turtle1.goto(x_val+(125-20/sqrt(2))*1/sqrt(2)+10+20+i*0.996194698092,-(screen_height/4)+(60/sqrt(2))+(120/sqrt(2)-20/sqrt(2))+200+20-i*0.087155742748-90)
        rectangleR(2, 2, "white", turtle1)
    
    
    return None


#HELPER VARIABLES
#getting window width and height
screen_width = screen.window_width()
screen_height = screen.window_height()
#getting min and max values of x and y
screen_min_x = -(screen_width / 2)
screen_max_x = (screen_width / 2)
screen_min_y = -(screen_height / 2)
screen_max_y = (screen_height / 2)


#BACKGROUND 
def draw_background():
     
    #draw sky "dodger blue" using rectangle function 
#     alex.penup()
    alex.pendown()
    alex.setheading(0)
    alex.goto(screen_min_x,screen_min_y)
    rectangleR(screen_width, screen_height, "dodgerblue", alex)
    
    #draw grass(lawngreen) using rectangle function
    alex.goto(screen_min_x,screen_min_y)
    rectangleR(screen_width, (screen_height/4), "lawngreen", alex)

    #draw sun using sunshine function
    sunshine(alex)

    #draw trees using rectangle and triangle functions
    x = -25
    for i in range(0,200,25):
#         x = randint((screen_min_x + 200),(screen_max_x - 100))
        alex.goto(x+2*i , -(screen_height/4))
        rectangleR(30, 300, "sienna", alex)
        for j in range(0,125,25):
            alex.goto((x-10), (-(screen_height/4)+200+j))
            triangle(100, "dark olive green", alex)
        x+=i
    return None








def main():
    for i in range(-400,1100,101):
        screen.tracer(False)
        draw_background()
        if i % 2 == 0:
            draw_robot2(alex, screen_min_x+i)
        else:
            draw_robot1(alex, screen_min_x+i)
        screen.tracer(True)
        sleep(0.5)
        screen.update()
    screen.tracer(False)
    draw_background()
    draw_robot3(alex, screen_min_x+1100)
    screen.tracer(True)
    
    screen.exitonclick()

    


main()
