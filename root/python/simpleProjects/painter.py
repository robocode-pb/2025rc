import turtle
turtle.shape("turtle")


def draw_star():
    size = int(input("What size of star?: "))
    fill_color = input("What color of star?: ")
    try:
        turtle.color(fill_color)  # Set the color
    except turtle.TurtleGraphicsError:
        print("There is no " + fill_color + " color")
        return
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def draw_square():
    size = int(input("What size of square?: "))
    color = input("What color of square?: ")
    try:
        turtle.color(color)  # Set the color
    except turtle.TurtleGraphicsError:
        print("There is no " + color + " color")
        return
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):  # Draw 4 sides of the square
        turtle.forward(size)  # Move forward by the specified size
        turtle.right(90)  # Rotate by 90 degrees
    turtle.end_fill()


def draw_circle():
    size = int(input("What size of circle?: "))
    fill_color = input("What color of circle?: ")
    try:
        turtle.color(fill_color)  # Set the color
    except turtle.TurtleGraphicsError:
        print("There is no " + fill_color + " color")
        return
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.circle(size)
    turtle.end_fill()


def clear():
    turtle.clear()


def set_speed(s):
    turtle.speed(s)


def set_shape(s):
    turtle.shape(s)

def draw_flag():
    size = int(input("What size of square?: "))
    color = "yellow"
    try:
        turtle.color(color)  # Set the color
    except turtle.TurtleGraphicsError:
        print("There is no " + color + " color")
        return
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):  # Draw 4 sides of the square
        turtle.forward(size)  # Move forward by the specified size
        turtle.right(90)  # Rotate by 90 degrees
    turtle.end_fill()

    color = "blue"
    try:
        turtle.color(color)  # Set the color
    except turtle.TurtleGraphicsError:
        print("There is no " + color + " color")
        return
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):  # Draw 4 sides of the square
        turtle.forward(size)  # Move forward by the specified size
        turtle.right(-90)  # Rotate by 90 degrees
    turtle.end_fill()
