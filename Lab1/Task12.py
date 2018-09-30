"""Draw smile"""

import turtle

def draw_face(radius, colors):
    turtle.penup()
    turtle.goto(radius, 0)
    turtle.pendown()
    turtle.color(*colors)
    turtle.begin_fill()
    turtle.seth(90)
    turtle.circle(radius)
    turtle.end_fill()


def draw_eyes(radius, colors):
    turtle.penup()
    turtle.goto(-(radius/3), radius/3)
    turtle.pendown()
    turtle.color(*colors)
    turtle.begin_fill()
    turtle.seth(90)
    turtle.circle(radius/10)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(radius/3, radius/3)
    turtle.pendown()
    turtle.color(*colors)
    turtle.begin_fill()
    turtle.seth(90)
    turtle.circle(-radius/10)
    turtle.end_fill()


def draw_nose(radius, color, default_width):
    turtle.penup()
    turtle.goto(0, radius/10)
    turtle.pendown()
    turtle.color(color)
    turtle.seth(270)
    turtle.color(color)
    turtle.width(10)
    turtle.forward(radius/10*2)
    turtle.color('black')
    turtle.width(default_width)


def draw_mouth(radius, color, default_width):
    turtle.penup()
    turtle.goto(-radius/2, -radius/3)
    turtle.pendown()
    turtle.color(color)
    turtle.seth(270)
    turtle.width(10)
    turtle.circle(radius/2, 180)
    turtle.width(default_width)



def smile(
        radius,
        default_width=1,
        eye_colors=("black", "blue"),
        face_colors=("black", "yellow"),
        nose_color="red",
        mouth_color="green"):
    draw_face(radius, face_colors)
    draw_eyes(radius, eye_colors)
    draw_nose(radius, nose_color, default_width)
    draw_mouth(radius, mouth_color, default_width)


smile(100)
