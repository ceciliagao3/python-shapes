from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
fillcolor("orchid")
begin_fill()
for t in range (10):
    pendown()
    pencolor("coral")
    left(36)
    forward(123)
end_fill()
x_pos = 40
y_pos = 40
fillcolor("honeydew")
begin_fill()
for t in range (10):
    pendown()
    pencolor("firebrick")
    left(36)
    forward(123)
end_fill()
# Close window on click.
exitonclick()
