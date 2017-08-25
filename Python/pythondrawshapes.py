from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
t.width(5)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
for jesushelpme in range(0,100):
    t.pendown()
    t.goto(0,0)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.back(90)
    t.rt(80)

# Close window on click.
#sth must be indented to be in a for loop
angle = 90
angle = angle + 5
angle = angle + 10
angle = angle + 15
#update values in a for loop??????
# angle gets angle= angle+5
#can reuse variablesahbroskis
exitonclick()
side = 10

for i in range(3):
    side = side + 5
    t.foward(50)
    t.pencolor("green")
    #ask user for input

user_side_length = input("How long sides?")
