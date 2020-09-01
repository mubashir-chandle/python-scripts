# 2020-09-1
'''Create a fractal tree using the turtle module.'''

import turtle

t = turtle.Turtle()

# Initialize starting position
t.hideturtle()
t.penup()
t.speed('fastest')
t.setpos(0, -250)
t.setheading(90)
t.pendown()

# Tunable Paramters
starting_length = 100
min_length = 1
angle = 30
length_factor = 0.55  # Length's proportion for the next recursive call


def fractal(starting_pos, starting_heading, length):
    if length < min_length:
        return

    # Initialize starting position for current recursive call.
    t.penup()
    t.setpos(starting_pos)
    t.setheading(starting_heading)
    t.pendown()

    # Create right-half.
    t.forward(length)
    t.right(angle)
    t.forward(length)
    right_pos = t.pos()
    right_heading = t.heading()

    # Reset turtle's position back to the starting position.
    t.penup()
    t.setpos(starting_pos)
    t.setheading(starting_heading)
    t.pendown()

    # Create left-half.
    t.forward(length)
    t.left(angle)
    t.forward(length)
    left_pos = t.pos()
    left_heading = t.heading()

    fractal(right_pos, right_heading, length * length_factor)
    fractal(left_pos, left_heading, length * length_factor)


fractal(t.pos(), t.heading(), starting_length)

turtle.mainloop()
