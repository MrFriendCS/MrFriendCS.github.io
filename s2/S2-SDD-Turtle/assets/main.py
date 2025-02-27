# Title: S2 SDD Turtle
# Author: Mr Friend
# Date: 26 Feb 2025

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

# Add a flower
tim.pu()
tim.goto(100, -200)
tim.pd()
tim.color("green")
tim.goto(100, -150)

# Add petals
for step in range(5):
    tim.circle(10)
    tim.left(360 / 5)
    


