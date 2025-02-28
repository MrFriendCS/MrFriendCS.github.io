# Title: S2 SDD Turtle
# Author: Mr Friend
# Date: 28 Feb 2025

# Get code to use a turtle
import turtle

# Create a turtle and give it a name
tim = turtle.Turtle()
tim.shape("turtle")
tim.color("brown")

# Move slowly
tim.speed(5)

# Walls
tim.goto(150, 0)
tim.goto(150, 125)

# Roof
tim.begin_fill()
tim.color("black")
tim.goto(0, 200)
tim.goto(-150, 125)
tim.end_fill()

# Walls
tim.color("brown")
tim.goto(-150, 0)
tim.home()

# Front door
tim.begin_fill()
tim.color("blue")
tim.left(90)
tim.fd(75)
tim.right(90)
tim.fd(50)
tim.right(90)
tim.fd(75)
tim.end_fill()

# Door handle
tim.pu()
tim.setheading(135)
tim.fd(50)
tim.dot(5, "red")

# Add a flower
tim.pu()
tim.goto(50, -150)

# Add stem
tim.color("pink")
tim.pd()
tim.goto(50, -100)

# Add petals
tim.color("green")

for step in range(5):
    tim.circle(10)
    tim.left(360/5)


    


