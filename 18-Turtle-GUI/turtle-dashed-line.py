import turtle as t

timmy = t.Turtle()

for i in range(50):
    if i % 2 == 0:
        timmy.pd()
        timmy.forward(5)
    else:
        timmy.pu()
        timmy.forward(5)
t.exitonclick()
