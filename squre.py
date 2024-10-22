import turtle
turtle.Screen().bgcolor("pink")
squre=turtle.Turtle()
squre.fillcolor("lightyellow")
squre.begin_fill()
# squre.forward(100)
# squre.left(90)
# squre.forward(100)
# squre.left(90)
# squre.forward(100)
# squre.left(90)
# squre.forward(100)
# squre.left(90)
for i in range(4):
    squre.forward(100)
    squre.left(90)
squre.end_fill()
turtle.done()


