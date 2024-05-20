import turtle
import time  # Needed for delays

# Opgavebeskrivelse:
# Opret et animeret grafisk analogt ur ved hjælp af turtle-modulet i Python.
# Uret skal mindst have en sekund- og minutviser.
# For hvert sekund skal den lange viser rotere et sekundstik.
# For hvert minut skal den korte viser rotere et minutstik.

# Initial setup
screen = turtle.Screen()  # This creates a handle to the screen
screen.tracer(0)  # This disables the drawing animation of the turtle
turtle.hideturtle()  # This hides the turtle symbol
screen.setup(width=800, height=800)
screen.title("Analog Clock")

# Create turtles for hour, minute, and second hands
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

for hand in [hour_hand, minute_hand, second_hand]:
    hand.hideturtle()
    hand.speed(0)
    hand.penup()

hour_hand.color("black")
minute_hand.color("blue")
second_hand.color("red")

# Function to draw the clock face
def draw_clock_face():
    turtle.penup()
    turtle.goto(0, -350)
    turtle.pendown()
    turtle.circle(350)
    for i in range(12):
        angle = i * 30
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90 - angle)
        turtle.forward(300)
        turtle.pendown()
        turtle.forward(30)
        turtle.penup()
        turtle.forward(20)
        turtle.write(i + 1, align="center", font=("Arial", 18, "normal"))

# Function to draw hands of the clock
def draw_hand(t, length, angle):
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(angle)
    t.pendown()
    t.forward(length)

# Main loop to update the clock every second
while True:
    current_time = time.localtime()
    second_angle = (current_time.tm_sec / 60) * 360
    minute_angle = (current_time.tm_min / 60) * 360 + (second_angle / 60)
    hour_angle = (current_time.tm_hour % 12 / 12) * 360 + (minute_angle / 12)

    screen.clear()
    draw_clock_face()
    draw_hand(second_hand, 300, second_angle)
    draw_hand(minute_hand, 250, minute_angle)
    draw_hand(hour_hand, 200, hour_angle)

    screen.update()
    time.sleep(1)
