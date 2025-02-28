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
tim.speed(1)

# Walls
tim.goto(150, 0)
tim.goto(150, 125)

# Roof
tim.color("black")
tim.goto(0, 200)
tim.goto(-150, 125)

# Walls
tim.color("brown")
tim.goto(-150, 0)
tim.home()

# Front door
tim.color("blue")
tim.left(90)
tim.fd(75)
tim.right(90)
tim.fd(50)
tim.right(90)
tim.fd(75)

# Door handle
tim.pu()
tim.setheading(135)
tim.fd(50)


    


