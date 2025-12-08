# Title: Xmas Turtle
# Author: Mr Friend
# Date: 20 Dec 2018

import turtle # gets the turtle code

# Trunk coordinates
treeTrunk = [[-40,-80],[40,-80],[40,-180],[-40,-180]]

# Branches coordinates
treeBranchesLeft = [[0,-80],[-160,-80],[-40,-30],[-140,-30],[-40,20],[-120,20],[-40,70],[-100,70],[-40,120],[-80,120],[0,180]]
treeBranchesRight = [[0,-80],[160,-80],[40,-30],[140,-30],[40,20],[120,20],[40,70],[100,70],[40,120],[80,120],[0,180]]

# Baubles
baublesLeft = [[-160,-80],[-140,-30],[-120,20],[-100,70],[-80,120]]
baublesRight = [[160,-80],[140,-30],[120,20],[100,70],[80,120]]

# setup window
window = turtle.Screen()
window.bgcolor("spring green")
window.title("Xmas Tree") # gives the window a title
window.setup(width=600, height=440, startx=350, starty=100) # creates a window for the turtle to live in

# setup turtle
tim = turtle.Turtle() # creates a turtle named tim
tim.shape("turtle")
tim.speed(1) # 1 slow - 10 fast (0 off)

# Trunk
tim.pu()
tim.goto(treeTrunk[0][0], treeTrunk[0][1])
tim.pd()
tim.color("brown")
tim.begin_fill()
for coord in treeTrunk:
    tim.goto(coord[0], coord[1])
tim.goto(treeTrunk[0][0], treeTrunk[0][1])
tim.end_fill()

# Branches - left
tim.pu()
tim.goto(treeBranchesLeft[0][0], treeBranchesLeft[0][1])
tim.pd()
tim.color("green")
tim.begin_fill()
for coord in treeBranchesLeft:
    tim.goto(coord[0], coord[1])
tim.goto(treeBranchesLeft[0][0], treeBranchesLeft[0][1])
tim.end_fill()

# Branches - right
tim.pu()
tim.goto(treeBranchesRight[0][0], treeBranchesRight[0][1])
tim.pd()
tim.color("green")
tim.begin_fill()
for coord in treeBranchesRight:
    tim.goto(coord[0], coord[1])
tim.goto(treeBranchesRight[0][0], treeBranchesRight[0][1])
tim.end_fill()

# Buables - left
tim.color("yellow")
for coord in baublesLeft:
    tim.pu()
    tim.goto(coord[0], coord[1]-20)
    tim.pd()
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()

# Buables - right
tim.color("red")
for coord in baublesRight:
    tim.pu()
    tim.goto(coord[0], coord[1]-20)
    tim.pd()
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()


tim.hideturtle()