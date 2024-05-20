import turtle

# Setup the turtle
t = turtle.Turtle()
t.speed(1)  # You can set the speed from 1 (slowest) to 10 (fastest)

# Function to draw the letter J
def draw_J():
    t.penup()
    t.goto(-50, 50)  # Starting point for J
    t.pendown()
    t.right(90)
    t.forward(100)  # Vertical line
    t.circle(-50, 180)  # Bottom curve of J
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.pendown()

# Function to draw the letter A
def draw_A():
    t.penup()
    t.goto(0, -50)  # Starting point for A
    t.pendown()
    t.left(75)
    t.forward(100)  # Left side of A
    t.right(150)
    t.forward(100)  # Right side of A
    t.backward(50)
    t.right(105)
    t.forward(30)  # Crossbar of A
    t.penup()
    t.backward(30)
    t.left(105)
    t.forward(50)
    t.right(75)

# Draw the initials
draw_J()
t.penup()
t.goto(-10, 0)
t.setheading(0)
draw_A()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
