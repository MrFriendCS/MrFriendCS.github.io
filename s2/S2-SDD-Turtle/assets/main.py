# Title: S2 SDD Turtle
# Author: Mr Friend
# Date: 25 Feb 2025

# Get code to use a turtle
import turtle

# Create a turtle and give it a name
tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")

# draw outline of house
tim.goto(150, 0)
tim.goto(150, 125)
tim.goto(0, 200)

tim.penup()

tim.goto(-150, 125)

tim.pendown()

tim.goto(-150, 0)
tim.home()
