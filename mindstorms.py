import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple")
    brad.speed(2)

    draw_square(brad)
    draw_circle(brad)
    draw_triangle(brad)

    window.exitonclick()


def draw_square(some_turtle):
    for times in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_circle(some_turtle):
    some_turtle.circle(100)


def draw_triangle(some_turtle):
    for times in range(0, 2):
        some_turtle.forward(100)
        some_turtle.right(90)
    some_turtle.right(45)
    some_turtle.forward(145)


def draw_final_art(some_turtle, times):
    some_turtle.speed(10)
    for i in range(0, times):
        draw_square(some_turtle)
        some_turtle.right(10)


draw_final_art(turtle.Turtle(), 50)
