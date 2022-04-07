"""
Introduction to Object-Oriented Programming in Python

    turtle is build-in graphic python module https://docs.python.org/3/library/turtle.html
        Turtle : build-in python class
        Screen : is a class, represent a canvas or windows object to draw turtle

    https://docs.python.org/3/library/turtle.html#turtle.shape
        available shape : “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
    https://docs.python.org/3/library/turtle.html#turtle.color
"""

from turtle import Turtle, Screen

raphael = Turtle()

raphael.shape("turtle")
raphael.color("green")
raphael.forward(100)

print(raphael)

myscreen = Screen()

# screen has attribute canvas height : canvheight, canvwidth
print(str(myscreen.canvheight) + " " + str(myscreen.canvwidth))

# this method will exit until you click on exit on canvas
myscreen.exitonclick()


