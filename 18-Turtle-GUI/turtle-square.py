# import turtle
# we can use from turtle import *
# but it doesn't recommend to use if you have a lot of packages installed
# or if you use module once or twice

# or we can use alias name
# especially it useful for long names
import turtle as t  # t is the alias name

while True:
    t.forward(100)
    t.right(90)
    if abs(t.pos()) < 1:
        break
t.done()
