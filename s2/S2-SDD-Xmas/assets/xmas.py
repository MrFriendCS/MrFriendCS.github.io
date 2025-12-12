# Title: Xmas Shapes
# Author: Mr Friend
# Date: 10 Dec 2025

# Get turtle code
import turtle

# Initial turtle settings
turtle.hideturtle()
turtle.shape("turtle")


def start(x, y):
    """Move to start position and get ready."""
    
    turtle.color("red")
    turtle.width(2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.showturtle()


def end():
    """Hides the turtle."""
    
    turtle.hideturtle()


def rectangle(x=0, y=0, width=40, height=0, colour="", thickness=0, fill=""):
    """Draws a rectangle."""

    # Set up
    start(x, y)
    
    # Draw a square
    if height == 0:
        height = width
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if thickness != 0:
        turtle.width(thickness)
    
    # Draw the rectangle / square
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    
    # End fill
    if fill != "":
        turtle.end_fill()
        
    end()


def triangle(x=0, y=0, width=40, height=0, colour="", thickness=0, fill=""):
    """Draws a triangle."""

    # Set up
    start(x, y)
    
    # Set the height
    if height == 0:
        height = width/2
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if thickness != 0:
        turtle.width(thickness)
    
    # Draw the triangle
    turtle.forward(width)
    turtle.goto(turtle.position()[0]-width/2, turtle.position()[1]+height)
    turtle.goto(turtle.position()[0]-width/2, turtle.position()[1]-height)
    
    # End fill
    if fill != "":
        turtle.end_fill()
        
    end()


def leftTri(x=0, y=0, width=40, height=0, colour="", thickness=0, fill=""):
    """Draws a left sided right-angle triangle."""

    # Set up
    start(x, y)
    
    # Set the height
    if height == 0:
        height = width
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen thickness
    if thickness != 0:
        turtle.width(thickness)
    
    # Draw the triangle
    turtle.forward(width)
    turtle.goto(turtle.position()[0]-width, turtle.position()[1]+height)
    turtle.goto(turtle.position()[0], turtle.position()[1]-height)
    
    # End fill
    if fill != "":
        turtle.end_fill()
        
    end()
        

def rightTri(x=0, y=0, width=40, height=0, colour="", thickness=0, fill=""):
    """Draws a right sided right-angle triangle."""

    # Set up
    start(x, y)
    
    # Set the height
    if height == 0:
        height = width/2
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if width != 0:
        turtle.width(thickness)
    
    # Draw the triangle
    turtle.forward(width)
    turtle.goto(turtle.position()[0], turtle.position()[1]+height)
    turtle.goto(turtle.position()[0]-width, turtle.position()[1]-height)
    
    # End fill
    if fill != "":
        turtle.end_fill()
        
    end()


def circle(x=0, y=0, radius=20, colour="", thickness=0, fill=""):
    """Draws a circle."""

    # Set up
    start(x, y)
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if thickness != 0:
        turtle.width(thickness)
    
    # Draw the circle
    turtle.circle(radius)
    
    # End fill
    if fill != "":
        turtle.end_fill()
        
    end()


def line(x1=0, y1=0, x2=50, y2=50, colour="", thickness=0):
    """Draws a line."""
    
    # Set up
    start(x1, y1)
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set pen width
    if thickness != 0:
        turtle.width(thickness)
    
    # Draw the line
    turtle.goto(x2, y2)
    
    end()
    

def star(x=0, y=0, colour="", scale=1):
    """Draws a star."""
    
    # Set up
    start(x, y)
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Start fill
    turtle.begin_fill()
    
    # First part
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(turtle.xcor()+15*scale, turtle.ycor()+30*scale)
    turtle.goto(turtle.xcor()+15*scale, turtle.ycor()-30*scale)
    turtle.goto(turtle.xcor()-15*scale, turtle.ycor()+10*scale)
    turtle.end_fill()
    
    # Second part
    turtle.begin_fill()
    turtle.goto(turtle.xcor()-20*scale, turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor()+40*scale, turtle.ycor())
    turtle.goto(turtle.xcor()-20*scale, turtle.ycor()-10*scale)    
    turtle.end_fill()
    
    # End fill
    turtle.end_fill()
        
    end()
    

def tree(x=0, y=0, scale=1, fir="", trunk=""):
    """Draws a tree."""
    
    # Set up
    start(x, y)

    # Trunk
    
    # Set trunk colour
    if trunk != "":
        turtle.color(trunk)
    else:
        turtle.color("brown")
    
    turtle.begin_fill()
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-30*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+30*scale)
    turtle.end_fill()
    
    # Branches
    
    # Set fir colour
    if fir != "":
        turtle.color(fir)
    else:
        turtle.color("green")

    turtle.begin_fill()
    turtle.goto(turtle.xcor()-40*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+40*scale, turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()-30*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+30*scale, turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()-20*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+20*scale, turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+15*scale, turtle.ycor()+20*scale)    
    turtle.goto(turtle.xcor()+15*scale, turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+20*scale, turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-20*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+30*scale, turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-30*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+40*scale, turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-50*scale, turtle.ycor())
    turtle.end_fill()
        
    end()
    

def snowman(x=0, y=0, scale=1, buttons="", eyes="", body="", head=""):
    """Draws a snowman."""
    
    # Set up
    start(x, y)
    
    # Set pen colour
    turtle.color("black")
    
    # Body
    
    # Set body fill colour
    if body != "":
        turtle.fillcolor(body)
    else:
        turtle.fillcolor("white")
    
    turtle.begin_fill()
    turtle.circle(20*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()+40*scale)
    turtle.pendown()
    
    # Head
    
    # Set body fill colour
    if head != "":
        turtle.fillcolor(head)
    elif body != "":
        turtle.fillcolor(body)
    else:
        turtle.fillcolor("white")
    
    turtle.begin_fill()
    turtle.circle(10*scale)
    turtle.end_fill()
    
    # Left eye
    if eyes != "":
        turtle.pencolor(eyes)
        turtle.fillcolor(eyes)
    else:
        turtle.pencolor("black")
        turtle.fillcolor("black")
    
    turtle.penup()
    turtle.goto(turtle.xcor()-5*scale, turtle.ycor()+10*scale)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    # Right eye
        
    turtle.penup()
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.pendown()
      
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    # Buttons colour
    if buttons != "":
        turtle.pencolor(buttons)
        turtle.fillcolor(buttons)
    else:
        turtle.pencolor("red")
        turtle.fillcolor("red")
    
    # Top button
    turtle.penup()
    turtle.goto(turtle.xcor()-5*scale, turtle.ycor()-20*scale)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    # Middle button   
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()-10*scale)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    # Bottom button   
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()-10*scale)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    
    end()


def snowwoman(x=0, y=0, scale=1, buttons="", eyes="", body="", head=""):
    """Draws a snowwoman."""
    
    snowman(x, y, scale, buttons, eyes, body, head)
    
    
def snowperson(x=0, y=0, scale=1, buttons="", eyes="", body="", head=""):
    """Draws a snowperson."""
    
    snowman(x, y, scale, buttons, eyes, body, head)
    

def snowchild(x=0, y=0, scale=1, buttons="", eyes="", body="", head=""):
    """Draws a snowperson."""
    
    snowman(x, y, scale/2, buttons, eyes, body, head)
    

def reindeer(x=0, y=0, scale=1, fur="", legs="", eye="", nose=""):
    """Draws a reindeer."""
    
    # Set up
    start(x, y)
    
    turtle.begin_fill()
    
    # Legs colour
    if legs != "":
        turtle.pencolor(legs)
        turtle.fillcolor(legs)
    else:
        turtle.pencolor("black")
        turtle.fillcolor("black")
    
    # Back Leg
    turtle.begin_fill()
    turtle.goto(turtle.xcor(), turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-5*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()+5*scale, turtle.ycor())
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()-25*scale, turtle.ycor())
    
    # Front leg
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(turtle.xcor(), turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-5*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()+5*scale, turtle.ycor())
    turtle.end_fill()
    
    #Body & Head
    
    # Fur colour
    if fur != "":
        turtle.pencolor(fur)
        turtle.fillcolor(fur)
    else:
        turtle.pencolor("brown")
        turtle.fillcolor("brown")
    
    turtle.begin_fill()
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+30*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()+20*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-30*scale)    
    turtle.goto(turtle.xcor()+30*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()-40*scale, turtle.ycor())
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()+40*scale)
    
    # Eye
    
    # Eye colour
    if eye != "":
        turtle.pencolor(eye)
        turtle.fillcolor(eye)
    else:
        turtle.pencolor("black")
        turtle.fillcolor("black")
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5*scale)
    turtle.end_fill()
    
    # Nose
    
    turtle.penup()
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor()-6*scale)
    
    # Nose colour
    if nose != "":
        turtle.pencolor(nose)
        turtle.fillcolor(nose)
    else:
        turtle.pencolor("black")
        turtle.fillcolor("black")
    
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3*scale)
    turtle.end_fill()
    
    
    
    end()
    
    
def santa(x=0, y=0, scale=1, suit="", hat="", gloves="", boots="", eyes=""):
    """Draws Santa."""
    
    # Set up
    start(x, y)
    
    # Left boot
    if boots != "":
        turtle.color(boots)
    else:
        turtle.color("black")
        
    turtle.begin_fill()
    turtle.goto(turtle.xcor(), turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-10*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()+10*scale)
    
    # Left boot fur
    turtle.pendown()
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+5*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-5*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor()-10*scale)
    
    # Right boot
    if boots != "":
        turtle.color(boots)
    else:
        turtle.color("black")
    
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.goto(turtle.xcor(), turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-10*scale)
    turtle.end_fill()
      
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()+10*scale)
    
    # Right boot fur
    turtle.pendown()
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+5*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-5*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()+5*scale)
    
    # Body
    if suit != "":
        turtle.color(suit)
    else:
        turtle.color("red")
        
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.goto(turtle.xcor(), turtle.ycor()+25*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor()-10*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor()-20*scale, turtle.ycor()+20*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-10*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor())
    turtle.goto(turtle.xcor()-20*scale, turtle.ycor()-20*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor(), turtle.ycor()-25*scale) # bottom left
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()-10*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor()+20*scale)
    
    # Belt
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.goto(turtle.xcor(), turtle.ycor()-5*scale)
    turtle.goto(turtle.xcor()-30*scale, turtle.ycor())
    turtle.goto(turtle.xcor(), turtle.ycor()+5*scale)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(turtle.xcor()-15*scale, turtle.ycor()-10*scale)

    # Left glove
    if gloves != "":
        turtle.color(gloves)
    else:
        turtle.color("black")
        
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(5*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()+60*scale, turtle.ycor())

    # Right glove
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(5*scale)
    turtle.end_fill()
        
    turtle.penup()
    turtle.goto(turtle.xcor()-30*scale, turtle.ycor()+35*scale)

    # Head
    turtle.pendown()
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.circle(10*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()-5*scale, turtle.ycor()+7*scale)

    # Left eye
    if eyes != "":
        turtle.color(eyes)
    else:
        turtle.color("black")
        
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())

    # Right eye
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(2*scale)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(turtle.xcor()-5*scale, turtle.ycor()+10*scale)
    
    # Hat
    if hat != "":
        turtle.color(hat)
    elif suit != "":
        turtle.color(suit)
    else:
        turtle.color("red")
        
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.goto(turtle.xcor()+10*scale, turtle.ycor())
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor()+10*scale)
    turtle.goto(turtle.xcor()-10*scale, turtle.ycor()-10*scale)
    turtle.end_fill()
    
    end()
    

def message(x=0, y=0, text="Merry Xmas!", size=14, colour=""):
    """Write a message."""
     
    # Set up
    start(x, y)
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Write message
    turtle.write(text, True, align="left", font=("Arial", size, "bold"))
        
    end()


def image(option=0):
    """Shows an grid."""
    
    noOfImages = 3
    
    choice = "image" + str(option % noOfImages) + ".png"
    
    turtle.Screen().bgpic(choice)
        
    end()
    

def background(colour="lightgreen"):
    """Set the background colour."""
    
    turtle.Screen().bgcolor(colour)
        
    end()


def fast():
    """Set the turtle speed to fast."""
    turtle.speed(10)


def medium():
    """Set the turtle speed to normal."""
    turtle.speed(6)


def slow():
    """Set the turtle speed to slow."""
    turtle.speed(1)


def medium():
    """Set the turtle speed to normal."""
    turtle.speed(6)
