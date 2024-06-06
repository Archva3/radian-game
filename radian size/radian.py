import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.title("Understanding Radians")
screen.bgcolor("lightblue")

# Setup turtle
t = turtle.Turtle()
t.speed(1)

# Function to draw a circle and the radius
def draw_circle(radius):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Function to draw an angle
def draw_angle(degrees):
    radians = math.radians(degrees)
    arc_length = radius * radians
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    t.forward(radius)
    t.left(90)
    t.circle(radius, degrees)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    t.forward(radius)
    t.write(f"{degrees} degrees = {round(radians, 2)} radians", align="left", font=("Arial", 12, "normal"))

# Main game loop
def main():
    global radius
    radius = 100
    draw_circle(radius)

    while True:
        try:
            degrees = int(screen.textinput("Input", "Enter an angle in degrees (0 to 360):"))
            if 0 <= degrees <= 360:
                t.clear()
                draw_circle(radius)
                draw_angle(degrees)
            else:
                t.write("Please enter a value between 0 and 360", align="center", font=("Arial", 12, "normal"))
        except:
            break

# Start the game
main()
screen.mainloop()