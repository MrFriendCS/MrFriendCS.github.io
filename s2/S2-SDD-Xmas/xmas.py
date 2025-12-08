# Title: Xmas Shapes
# Author: Mr Friend
# Date: 5 Dec 2025

# Get turtle code
import turtle
   
   
def start(x, y):
    """Move to start position and get ready."""
    turtle.color("red")
    turtle.width(2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()


def rectangle(x=0, y=0, w=40, h=0, colour="", width=0, fill=""):
    """Draws a rectangle."""

    # Set up
    start(x, y)
    
    # Draw a square
    if h == 0:
        h = w
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if width != 0:
        turtle.width(width)
    
    # Draw the rectangle / square
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    
    # End fill
    if fill != "":
        turtle.end_fill()


def triangle(x=0, y=0, w=40, h=0, colour="", width=0, fill=""):
    """Draws a triangle."""

    # Set up
    start(x, y)
    
    # Set the height
    if h == 0:
        h = w/2
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if width != 0:
        turtle.width(width)
    
    # Draw the triangle
    turtle.forward(w)
    turtle.goto(turtle.position()[0]-w/2, turtle.position()[1]+h)
    turtle.goto(turtle.position()[0]-w/2, turtle.position()[1]-h)
    
    # End fill
    if fill != "":
        turtle.end_fill()


def leftTri(x=0, y=0, w=40, h=0, colour="", width=0, fill=""):
    """Draws a left sided right-angle triangle."""

    # Set up
    start(x, y)
    
    # Set the height
    if h == 0:
        h = w/2
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if width != 0:
        turtle.width(width)
    
    # Draw the triangle
    turtle.forward(w)
    turtle.goto(turtle.position()[0]-w, turtle.position()[1]+h)
    turtle.goto(turtle.position()[0], turtle.position()[1]-h)
    
    # End fill
    if fill != "":
        turtle.end_fill()
        

def rightTri(x=0, y=0, w=40, h=0, colour="", width=0, fill=""):
    """Draws a right sided right-angle triangle."""

    # Set up
    start(x, y)
    
    # Set the height
    if h == 0:
        h = w/2
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Set fill colour
    if fill != "":
        turtle.fillcolor(fill)
        turtle.begin_fill()
    
    # Set pen width
    if width != 0:
        turtle.width(width)
    
    # Draw the triangle
    turtle.forward(w)
    turtle.goto(turtle.position()[0], turtle.position()[1]+h)
    turtle.goto(turtle.position()[0]-w, turtle.position()[1]-h)
    
    # End fill
    if fill != "":
        turtle.end_fill()


def circle(x=0, y=0, r=20, colour="", width=0, fill=""):
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
    if width != 0:
        turtle.width(width)
    
    # Draw the circle
    turtle.circle(r)
    
    # End fill
    if fill != "":
        turtle.end_fill()


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
    

def message(x=0, y=0, text="Merry Xmas!", size=14, colour=""):
    """Write a message."""
     
    # Set up
    start(x, y)
    
    # Set pen colour
    if colour != "":
        turtle.color(colour)
    
    # Write message
    turtle.write(text, True, align="left", font=("Arial", size, "bold"))


def grid():
    """Shows a 50x50 grid."""
    
    turtle.Screen().bgpic("grid.png")
    

def background(colour="lightgreen"):
    
    turtle.Screen().bgcolor(colour)

