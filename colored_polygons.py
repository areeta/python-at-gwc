#Instructions

#Add parameters to your square function to so that you can draw squares of different sizes and colors.

#Do the same thing for your triangle function.

#Recreate the following picture. Each square has a side of 50 pixels and are 10 pixels apart. You can pick whatever colors you want.

#Can you do the same thing with your triangles?

from turtle import *
penup()
goto(-200,200)
def square(size, pen_color, fill_color):
	pencolor(pen_color)
	fillcolor(fill_color)
	begin_fill()
	pendown()
	for i in range(4):
		speed(0)
		forward(size)
		right(90)
	end_fill()

square(400, "powderblue", "mintcream")
penup()
goto(-175,-100)
square(50, "purple", "white")
penup()
forward(60)
square(50, "blue", "white")
penup()
forward(60)
square(50, "salmon", "white")
penup()
forward(60)
square(50, "lightseagreen", "white")
penup()
forward(60)
square(50, "gold", "white")
penup()
forward(60)
square(50, "red", "white")
penup()
forward(60)

right(180)
forward(10)

def triangle(size, pen_color):
	pencolor(pen_color)
	pendown()
	for i in range(3):
		speed(0)
		forward(size)
		right(120)

triangle(50, "green")
penup()
forward(60)
triangle(50, "tan")
penup()
forward(60)
triangle(50, "pink")
penup()
forward(60)
triangle(50, "darkgrey")
penup()
forward(60)
triangle(50, "thistle")
penup()
forward(60)
triangle(50, "yellow")
penup()
forward(60)
 

#Write a function that can draw any regular polygon with any of the possible colors.
#A regular polygon is any shape where all the sides and all the internal angles are the same. A square is a regular polygon, a rectangle is not.
#What kind parameters will this function need? 
#The turtle draws the outside edges of the polygon. Each angle it draws will be a number of degrees that is (360 / number of sides).

#Hint: regular_polygon(4, 50 , “red”) should give something that looks like this: 

#Hint : regular_polygon(3, 50, “green”) should give something that looks like this:

#What happens if you call regular_polygon(100, 5, “red”)?

#You can make complex drawings just by repeating simple shapes at a slightly different angle or position each time. 
#The following the drawing was built by repeatedly calling regular_polygon(5, 20, “maroon”) but moving the turtle two pixels forward each time. 
#Trying playing around with repeated simple shapes but changing something small each time, like the angle the turtle is turned or where it is. 

goto(150, 150)
def polygon(sides, length, color):
	pencolor(color)
	pendown()
	for i in range(sides):
		speed(0)
		forward(length)
		right(360/sides)
		
polygon(5, 20, "purple")
penup()
goto(-130,160)
pendown()
pencolor("yellow")
fillcolor("yellow")
begin_fill()
circle(30)
end_fill()
penup()
goto(-130, 130)
for i in range(9):
	pendown()
	pencolor("yellow")
	right(40)
	forward(65)
	backward(65)

penup()

goto(0,0)
pencolor("black")
pendown()
circle(10)
circle(10, 180)
right(90)
forward(15)
left(90)
forward(10)
left(180)
forward(20)
right(180)
forward(20)
left(180)
forward(10)
right(270)
forward(20)
right(45)
forward(15)
right(180)
forward(15)
left(270)
forward(20)

penup()

goto(30,0)
pencolor("blue")
pendown()
circle(10)
circle(10,180)
right(90)
forward(15)
left(90)
forward(10)
left(180)
forward(20)
right(180)
forward(20)
left(180)
forward(10)
right(270)
forward(20)
right(45)
forward(15)
right(180)
forward(15)
left(270)
forward(20)

penup()

goto(-30,0)
pencolor("blue")
pendown()
circle(10)
circle(10,180)
right(90)
forward(15)
left(90)
forward(10)
left(180)
forward(20)
right(180)
forward(20)
left(180)
forward(10)
right(270)
forward(20)
right(45)
forward(15)
right(180)
forward(15)
left(270)
forward(20)

input()
			
