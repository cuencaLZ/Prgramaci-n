"""This series of katas will introduce you to basics of doing geometry with computers.

Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.

Write a function calculating circumference of a Circle.

Tests round answers to 6 decimal places."""

def circle_circumference(circle):
    x=circle.center.x
    y=circle.center.y
    r=circle.radius
    import math
    c= r*2*math.pi
    return c
    