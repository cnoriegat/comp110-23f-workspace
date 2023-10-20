"""Turtle tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)
leo.pencolor("pink")
leo.fillcolor(255, 232, 0)

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-150, 150)
leo.pendown()

i: int = 0
leo.begin_fill()
while i < 3:
    leo.forward(300)
    leo.right(120)
    i += 1
leo.end_fill()

leo.goto(-150, 150)

bob: Turtle = Turtle()

done()