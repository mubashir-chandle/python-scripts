# 2020-09-1
'''Create a 4-way fractal'''

import turtle

t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()

starting_length = 50
min_length = 12.5
length_factor = 0.5
starting_angle = 0


def fractal(starting_position, length, angle):
    if length < min_length:
        return

    t.setheading(angle)

    # Reset position
    t.penup()
    t.setpos(starting_position)
    t.pendown()

    # Top Section
    t.forward(length)
    t.right(45)
    t.forward(length)
    t.left(45)
    t.forward(length)
    top_pos = t.pos()

    # Reset position
    t.penup()
    t.setpos(starting_position)
    t.pendown()

    # Right Section
    t.right(90)
    t.forward(length)
    t.right(45)
    t.forward(length)
    t.left(45)
    t.forward(length)
    right_pos = t.pos()

    # Reset position
    t.penup()
    t.setpos(starting_position)
    t.pendown()

    # Down Section
    t.right(90)
    t.forward(length)
    t.right(45)
    t.forward(length)
    t.left(45)
    t.forward(length)
    down_pos = t.pos()

    # Reset position
    t.penup()
    t.setpos(starting_position)
    t.pendown()

    # Left Section
    t.right(90)
    t.forward(length)
    t.right(45)
    t.forward(length)
    t.left(45)
    t.forward(length)
    left_pos = t.pos()

    angle = 0 if angle == 45 else 45

    fractal(top_pos, length * length_factor, angle)
    fractal(right_pos, length * length_factor, angle)
    fractal(down_pos, length * length_factor, angle)
    fractal(left_pos, length * length_factor, angle)


fractal(t.pos(), starting_length, starting_angle)
turtle.mainloop()
