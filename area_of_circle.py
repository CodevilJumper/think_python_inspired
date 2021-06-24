# Incremental development example

# Area of the circle

def area(radius):
    a = math.pi * radius**2
    print('Area of the circle is', a)
    return a

# Calculates the distance between two points

import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    print('distance between two points is', result)
    return result

# Composition of functions

def circle_area(xc, yc, xp, yp):
    print('Calculating the area of the circle based on the distance between two points (radius) where:')
    return area(distance(xc, yc, xp, yp))

# Calling functions

circle_area(4, 3, 1, 3)


