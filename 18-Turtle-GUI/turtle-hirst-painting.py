import turtle as turtle_module
import random

# import colorgram

# color = colorgram.extract('image.jpg', 30)
#
# colors = []
# for i in range(0, len(color)):
#     colors.append(color[i].rgb)
#
# print([tuple(rgb) for rgb in colors])

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),
              (179, 17, 8), (233, 66, 34)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()

turtle_module.exitonclick()