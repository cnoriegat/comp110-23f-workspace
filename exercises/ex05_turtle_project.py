"""Turtle Scene Project!"""


__author__ = "730621572"


from turtle import Turtle, colormode, done, Screen
from random import randint


# setting the parameters of the screen and prompting for a name
screen = Screen()
screen.title("Welcome to the Andes!")
screen.setup (width=1200, height=1200, startx=0, starty=0)
your_name: str = screen.textinput("", "What is your name? ")

# defining my main function
def main() -> None:
    """The entrypoint of my scene."""
    sky()
    sun (0,-100)
    for elem in range(40):
        birds((randint(-600,600)),(randint(0,600)))
    mountains3(-450, -100)
    mountains2(-500, -100)
    mountains1(-600, -100)
    lake()
    welcome()
    done()


# defining functions for creating the scene
def welcome(bob: Turtle = Turtle()) -> None:
    """Formula to personalize welcome."""
    bob: Turtle = Turtle()

    bob.hideturtle()
    bob.penup()
    bob.pencolor("White")
    bob.goto(0, 0)

    bob.write(f"Welcome to the Andes, {your_name}!", align="center", font=("Verdana", 32, "normal"))
    bob.hideturtle()


def triangle(x: float, y: float, z: float, tom: Turtle = Turtle()) -> None:
    """Function to draw a triangle with given parameters"""
    idx: int = 0
    while idx < z:
        tom.forward(x)
        tom.right(y)
        tom.forward(x)
        tom.left(y)
        idx += 1


def rectangle(x: float, mia: Turtle = Turtle()) -> None:
    """Formula to make rectangles."""
    idx: int = 0
    while idx < 2:
        mia.forward(1200)
        mia.right(90)
        mia.forward(x)
        mia.right(90)
        idx += 1


def mountains1(x: float, y: float, harry: Turtle = Turtle()) -> None:
    """First set of mountains."""
   
    harry.speed(50)
    harry.hideturtle()
   
    harry.penup()
    harry.goto(x, y)
    harry.setheading(60)
    harry.pendown()

    colormode(255)
    harry.color(95, 141, 91)
    harry.fillcolor(95, 141, 91)   

    harry.begin_fill()
    triangle(200, 120, 6, harry)
    harry.end_fill()
    harry.penup()
    harry.pendown()


def mountains2(x: float, y: float, niall: Turtle = Turtle()) -> None:
    """Second set of mountains."""
    
    niall.speed(50)
    niall.hideturtle()
    
    niall.penup()
    niall.goto(x, y)
    niall.setheading(34)
    niall.pendown()

    colormode(255)
    niall.color(229, 151, 189)
    niall.fillcolor(229, 151, 189)
    niall.begin_fill()
    triangle(300, 68, 2, niall)
    niall.end_fill()


def mountains3(x: float, y: float, liam: Turtle = Turtle()) -> None:
    """Third mountain."""
    
    liam.speed(50)
    liam.hideturtle()
    
    liam.penup()
    liam.goto(x, y)
    liam.pendown()

    colormode(255)
    liam.color(244, 145, 63)
    liam.fillcolor(244, 145, 63)
    liam.left(60)
    liam.begin_fill()
    triangle(300, 120, 3, liam)
    liam.end_fill()


def sun(x: float, y: float, louis: Turtle = Turtle()) -> None:
    """The sun."""

    louis.speed(50)
    louis.hideturtle()

    colormode(255)
    louis.color(232, 185, 65)
    louis.fillcolor(232, 185, 65)
    
    louis.penup()
    louis.goto(x, y)
    louis.pendown()

    louis.begin_fill()
    louis.circle(200)
    louis.end_fill()


def birds(x: float, y: float, ron: Turtle = Turtle()) -> None:
    """Function to draw birds with random position""" 
    
    ron.speed(200)
    ron.hideturtle()
   
    ron.penup()
    ron.goto(x, y)
    ron.setheading(90)
    ron.pendown()

    colormode(255)
    ron.color("black")
    for elem in range(2):
        ron.circle(10, 180)
        ron.left(180)


def lake(zayn: Turtle = Turtle()) -> None:
    """Function to draw lake"""
    a: int = 60 
    b: int = 143
    c: int = 179
    idx: int = 0
    upd_start: int = -100

    while idx < 7: 
        zayn.speed(50)
        zayn.hideturtle()
        zayn.penup()
        zayn.goto(-600, upd_start)
        zayn.pendown()
        
        colormode(255)
        zayn.color(a, b, c)
        zayn.fillcolor(a, b, c)
        zayn.begin_fill()
        rectangle(50, zayn)
        zayn.end_fill()

        a -= 3
        b -= 3
        c -= 3
        
        upd_start -= 50
        idx += 1


def sky(ada: Turtle = Turtle()) -> None:
    """The Sky."""
    ada.speed(50)
    ada.hideturtle()

    colormode(255)
    ada.color(225, 245, 249)
    ada.fillcolor(225, 245, 249)
    
    ada.penup()
    ada.goto(-600, 600)
    ada.pendown()

    ada.begin_fill()
    rectangle(700, ada)
    ada.end_fill()


# running program
if __name__ == "__main__":
    main()