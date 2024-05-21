import turtle
import math

# Opsæt skærm
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Hit the target")

# Opsæt kanonen
gun = turtle.Turtle()
gun.color("black")
gun.shape("triangle")
gun.penup()
gun.speed(1)
gun.setposition(-200, 0)

# Opsæt målet
target = turtle.Turtle()
target.color("red")
target.shape("circle")
target.penup()
target.speed(0)
target.setposition(100, 0)

# Tegn målet
target.shapesize(2, 2)  # Målets størrelse er større

# Definer funktioner
def fire():
    angle = gun.heading()
    force = 50  # Dette kan være dynamisk baseret på brugerinput
    radian_angle = math.radians(angle)
    x = force * math.cos(radian_angle)
    y = force * math.sin(radian_angle)
    hit_target(x, y)

def hit_target(x, y):
    target_x = target.xcor()
    target_y = target.ycor()
    if target_x - 20 < x < target_x + 20 and target_y - 20 < y < target_y + 20:
        print("Target hit!")
    else:
        print("Missed!")
        give_hint(x, y, target_x, target_y)

def give_hint(x, y, target_x, target_y):
    if x < target_x - 20:
        print("Prøv en større vinkel eller mere kraft")
    elif x > target_x + 20:
        print("Prøv en mindre vinkel eller mindre kraft")
    elif y < target_y - 20:
        print("Prøv en større vinkel")
    elif y > target_y + 20:
        print("Prøv en mindre vinkel")

# Nøglebindinger
wn.listen()
wn.onkey(fire, "space")

# Hovedloop
wn.mainloop()
