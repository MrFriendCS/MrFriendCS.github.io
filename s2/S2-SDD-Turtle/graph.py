# Title: Turtle graph
# Author: Mr Friend
# Date: 22 Oct 2020

# Get turtle code
import turtle

# Create a turtle (called Tim)
tim = turtle.Turtle()

# Set the turtle's characteristics
tim.speed(0)
tim.pensize(1)
tim.color("grey")

# Draw vertical lines
for xValue in range(-300, 320, 20):
    tim.penup()
    tim.goto(xValue, -200)
    tim.pendown()
    tim.goto(xValue, 200)

# Draw horizontal lines
for yValue in range(-200, 220, 20):
    tim.penup()
    tim.goto(-300, yValue)
    tim.pendown()
    tim.goto(300, yValue)

# Draw x-axis
tim.penup()
tim.pensize(2)
tim.color("black")
tim.goto(-300, 0)
tim.pendown()
tim.goto(300, 0)

# Draw y-axis
tim.penup()
tim.goto(0, -200)
tim.pendown()
tim.goto(0, 200)

# Top coordinate
tim.penup()
tim.goto(0, 210)
tim.write("(0, 200)", True, align="center")

# Bottom coordinate
tim.goto(0, -215)
tim.write("(0, -200)", True, align="center")

# Left coordinate
tim.goto(-310, 0)
tim.write("(-300, 0)", True, align="right")

# Right coordinate
tim.goto(310, 0)
tim.write("(300, 0)", True, align="left")

# Move the turtle to the centre
tim.penup()
tim.goto(0,0)
tim.pendown()
tim.dot(4)

## Start your code here ##

