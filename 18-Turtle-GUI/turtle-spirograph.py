import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

heading = 10


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(heading)
    heading += 5

t.exitonclick()
