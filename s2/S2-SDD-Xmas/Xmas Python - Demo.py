# Title: Xmas Turtle
# Author: Mr Friend
# Date: 14 Dec 2018

def drawHouse(xStart, yStart, colourStart):

    tim.penup()
    tim.color(colourStart)
    tim.goto(xStart, yStart)

    # Ground floor
    tim.pendown()
    tim.begin_fill()
    tim.goto(tim.xcor()+100, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-50)
    tim.goto(tim.xcor()-100, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+50)
    tim.end_fill()
    
    # Roof
    tim.color("black")
    tim.begin_fill()
    tim.goto(tim.xcor()+50, tim.ycor()+30)
    tim.goto(tim.xcor()+50, tim.ycor()-30)
    tim.goto(tim.xcor()-100, tim.ycor())
    tim.end_fill()

    tim.penup()
    tim.goto(tim.xcor()+10, tim.ycor()-30)

    # Window
    tim.pendown()
    tim.color("white")
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()+20)
    tim.goto(tim.xcor()+20, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-20)
    tim.goto(tim.xcor()-20, tim.ycor())
    tim.end_fill()

    tim.penup()
    tim.goto(tim.xcor()+60, tim.ycor())

    # Window
    tim.pendown()
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()+20)
    tim.goto(tim.xcor()+20, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-20)
    tim.goto(tim.xcor()-20, tim.ycor())
    tim.end_fill()

    tim.penup()
    tim.goto(tim.xcor()-30, tim.ycor()-20)

    # Door
    tim.pendown()
    tim.color("brown")
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()+40)
    tim.goto(tim.xcor()+20, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-40)
    tim.end_fill()

def drawTree(xStart, yStart):
    
    tim.penup()
    tim.color("brown")
    tim.goto(xStart, yStart)

    # Trunk
    tim.pendown()
    tim.begin_fill()
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-30)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+30)
    tim.end_fill()
    
    # Branches
    tim.color("green")
    tim.begin_fill()
    tim.goto(tim.xcor()-40, tim.ycor())
    tim.goto(tim.xcor()+40, tim.ycor()+20)
    tim.goto(tim.xcor()-30, tim.ycor())
    tim.goto(tim.xcor()+30, tim.ycor()+20)
    tim.goto(tim.xcor()-20, tim.ycor())
    tim.goto(tim.xcor()+20, tim.ycor()+20)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor()+15, tim.ycor()+20)    
    tim.goto(tim.xcor()+15, tim.ycor()-20)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor()+20, tim.ycor()-20)
    tim.goto(tim.xcor()-20, tim.ycor())
    tim.goto(tim.xcor()+30, tim.ycor()-20)
    tim.goto(tim.xcor()-30, tim.ycor())
    tim.goto(tim.xcor()+40, tim.ycor()-20)
    tim.goto(tim.xcor()-50, tim.ycor())
    tim.end_fill()
    
    drawStar(tim.xcor()-10, tim.ycor()+65, 1)

def drawSanta(xStart, yStart):
     
    tim.penup()
    tim.color("black")
    tim.goto(xStart, yStart)

    # Reindeer
    tim.pendown()
    tim.begin_fill()
    
    # Back Leg
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()-20)
    tim.goto(tim.xcor()-5, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+20)
    tim.goto(tim.xcor()+5, tim.ycor())
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()-25, tim.ycor())
    
    # Front leg
    tim.pendown()
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()-20)
    tim.goto(tim.xcor()-5, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+20)
    tim.goto(tim.xcor()+5, tim.ycor())
    tim.end_fill()
    
    #Body & Head
    tim.color("brown")
    tim.begin_fill()
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+30)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+20)
    tim.goto(tim.xcor()+20, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-30)    
    tim.goto(tim.xcor()+30, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-20)
    tim.goto(tim.xcor()-40, tim.ycor())
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor(), tim.ycor()+40)
    
    # Eye
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.circle(5)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+70, tim.ycor()-25)
    
    # Sleigh body
    tim.pendown()
    tim.color("OrangeRed3")
    tim.begin_fill()
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor()+10, tim.ycor()-10)
    tim.goto(tim.xcor()+30, tim.ycor())
    tim.goto(tim.xcor()+10, tim.ycor()+20)
    tim.goto(tim.xcor()+20, tim.ycor())
    tim.goto(tim.xcor()-10, tim.ycor()-20)
    tim.goto(tim.xcor()+10, tim.ycor()-10)
    tim.goto(tim.xcor()-70, tim.ycor())
    tim.goto(tim.xcor()-10, tim.ycor()+20)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+20, tim.ycor()-20)
    
    # Sleigh skis
    tim.pendown()
    tim.color("yellow")
    tim.begin_fill()
    tim.goto(tim.xcor()-10, tim.ycor()-10)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor()-10, tim.ycor()+10)
    tim.goto(tim.xcor()-5, tim.ycor())
    tim.goto(tim.xcor()+15, tim.ycor()-15)
    tim.goto(tim.xcor()+90, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+5)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor()-10, tim.ycor()+10)
    tim.goto(tim.xcor()-5, tim.ycor())
    tim.goto(tim.xcor()+5, tim.ycor()-10)
    tim.goto(tim.xcor()-50, tim.ycor())
    tim.goto(tim.xcor()+10, tim.ycor()+10)
    tim.goto(tim.xcor()-5, tim.ycor())
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()-90, tim.ycor()+15)
    
    # Reigns
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.goto(tim.xcor()+90, tim.ycor())
    tim.goto(tim.xcor()+15, tim.ycor()+10)
    tim.goto(tim.xcor()-5, tim.ycor())
    tim.goto(tim.xcor()-10, tim.ycor()-5)
    tim.goto(tim.xcor()-90, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-5)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+170, tim.ycor()-30)
    
    # Santa
    
    # Left boot
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()+10)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-10)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor(), tim.ycor()+10)
    
    tim.pendown()
    tim.color("black", "white")
    tim.begin_fill()
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+5)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-5)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+10, tim.ycor()-10)
    
    # Right boot
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()+10)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-10)
    tim.end_fill()
      
    tim.penup()
    tim.goto(tim.xcor(), tim.ycor()+10)
    
    tim.pendown()
    tim.color("black", "white")
    tim.begin_fill()
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+5)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-5)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor(), tim.ycor()+5)
    
    # Body
    tim.pendown()
    tim.color("red")
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()+25)
    tim.goto(tim.xcor()+10, tim.ycor()-10)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor()-20, tim.ycor()+20)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+10)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-10)
    tim.goto(tim.xcor()-10, tim.ycor())
    tim.goto(tim.xcor()-20, tim.ycor()-20)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor()+10, tim.ycor()+10)
    tim.goto(tim.xcor(), tim.ycor()-25) # bottom left
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+10)
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()-10)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+10, tim.ycor()+20)
    
    # Belt
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.goto(tim.xcor(), tim.ycor()-5)
    tim.goto(tim.xcor()-30, tim.ycor())
    tim.goto(tim.xcor(), tim.ycor()+5)
    tim.end_fill()

    tim.penup()
    tim.goto(tim.xcor()-15, tim.ycor()-10)

    # Left hand
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.circle(5)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+60, tim.ycor())

    # Right hand
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.circle(5)
    tim.end_fill()
        
    tim.penup()
    tim.goto(tim.xcor()-30, tim.ycor()+35)

    # Head
    tim.pendown()
    tim.color("black", "white")
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()-5, tim.ycor()+7)

    # Left eye
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.circle(2)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()+10, tim.ycor())

    # Right eye
    tim.pendown()
    tim.color("black")
    tim.begin_fill()
    tim.circle(2)
    tim.end_fill()
    
    tim.penup()
    tim.goto(tim.xcor()-5, tim.ycor()+10)
    
    # Hat
    tim.pendown()
    tim.color("red")
    tim.begin_fill()
    tim.goto(tim.xcor()+10, tim.ycor())
    tim.goto(tim.xcor()-10, tim.ycor()+10)
    tim.goto(tim.xcor()-10, tim.ycor()-10)
    tim.end_fill()
    
    
    
def drawStar(xStart, yStart, scale):
     
    tim.penup()
    tim.color("yellow")
    tim.goto(xStart, yStart)

    # First part
    tim.pendown()
    tim.begin_fill()
    tim.goto(tim.xcor()+15*scale, tim.ycor()+30*scale)
    tim.goto(tim.xcor()+15*scale, tim.ycor()-30*scale)
    tim.goto(tim.xcor()-15*scale, tim.ycor()+10*scale)
    tim.end_fill()
    
    # Second part
    tim.begin_fill()
    tim.goto(tim.xcor()-20*scale, tim.ycor()+10*scale)
    tim.goto(tim.xcor()+40*scale, tim.ycor())
    tim.goto(tim.xcor()-20*scale, tim.ycor()-10*scale)    
    tim.end_fill()
    
def writeMessage(xStart, yStart):
     
    tim.penup()
    tim.goto(xStart,yStart)
    tim.color("red")
    tim.write("Merry Christmas!", True, align="left", font=("Arial", 14, "bold"))


import turtle # gets the turtles code

# setup window
window = turtle.Screen()
window.bgcolor("spring green")
window.title("Xmas Python") # gives the window a title
window.setup(width=600, height=440, startx=350, starty=100) # creates a window for the turtle to live in

# setup turtle
tim = turtle.Turtle() # creates a turtle named tim
tim.shape("turtle")
tim.color("red")
tim.speed(1) # 1 slow - 10 fast (0 off)

# Draw scene

drawHouse(-100, -130, "blue")
drawHouse(100, -70, "green")

drawTree(-220, -130)
drawTree(-160, -10)
drawTree(-10, -50)
drawTree(200, 20)

drawSanta(-20, 100)

drawStar(-260, 120, 3)

writeMessage(-130, 170)

tim.hideturtle()

window.exitonclick()