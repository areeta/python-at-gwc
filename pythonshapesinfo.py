'''
Some turtle functions you can use to make your shapes


forward(<distance>) - This function takes a positive or negative number and
will move the turtle forward.

back(<distance>) - This function takes a positive or negative numbers and
it will move the turtle back.

right(<angle>) - This function takes a number that represents
angle in degrees. It will turn the turtle to  its right

left(<angle>) - This functions takes an number that represents
 an angle in degrees. It will turn the turtle to its left.

pencolor(<color>) - This functions takes a string that represents a color. The
turtle's pen will draw in that color. The possible color values can be found
at https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

penup() - This function takes no parameters. When called it will
lift the turtle's pen up, the turtle will not draw when moved.

pendown() - This function takes no parameters. When called it will put the
turtle's pen down. It will draw when moved.

speed(<number>) - This function takes a number. It determines how fast the
turtle moves around the screen. Strangely enough if you want it to go as
fast as possible you have to pass it 0 as a parameter.

goto(<x>, <y>) - This function takes two numbers, a position along the x-axis
and a position along the y-axis. It will move the turtle to that position.

fillcolor(<color>) - This function takes a string that represents a color. The
color will be used to fill shape the turtle has made. In order to get the turtle
to fill the shape you have to use the begin_fill() function before the turtle
starts drawing the shape and the end_fill() function after it finishes for the
shape to be filled in.

begin_fill() - This function takes no parameters. It is put before the turtle
draws a shape that you want filled in.

end_fill() - This function takes no parameters. It is put after the turtle has
finished drawing a shape that you want filled in.

dot(<size>, <color>) - This function takes two parameters. The first is a
positive number that represents the diameter of the dot to be drawn by the
turtle. The second is a string that represents the color the dot should be.


BONUS:

circle(<radius>, <extent>, <steps>) - This function takes three parameters.
However you only have to put in the first one. The <radius> parameter is the
necessary parameter, it is a number that represents the radius of the circle.
The <extent> is optional. It represents an angle saying how much of the circle
should be drawn, if you don't put in anything for <extent> it will draw the whole
circle. If you put in 180, it will draw a half circle. The third parameter
<steps> is a number that represents how many steps the turtle should take to
draw the circle. Try setting <steps> as 5 to see what happens.


'''


from turtle import *

# START WRITING YOUR CODE HERE

#Download the starter code and familiarize yourself with its contents.
#Draw a square using the “forward”, “right” or “left” functions.
#Use a for loop so you don't have to repeat calling the forward and turning functions  so many times.  
#Store how big you would like the the side of the square to be in a variable called `side_length`. Use the variable in the `forward` function instead of writing the number in the for loop that makes a square.
#Use a for loop to draw an equilateral triangle.
#The turtle needs to go around the outside edges of the shape. In an equilateral triangle, the inside angle will be 60 degrees, so the turtle needs to turn 180 - 60 = 120 degrees


print("Please say how big you would like the sides of the squares to be in numerical form!")
side_length = int(input())
for i in range(4):
	pendown()
	forward(side_length)
	right(90)

penup()
go to (50, 50)

print("I finished drawing a square. Now, I will draw a triangle. Please give me sides in numberical forms!")
side_lengthh = int(input())
for i in range(3):
	pendown()
	forward(side_lengthh)
	right(120)
	
input()





