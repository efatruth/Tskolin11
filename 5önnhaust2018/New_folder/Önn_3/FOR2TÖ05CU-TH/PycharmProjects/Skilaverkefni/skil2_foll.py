import math

def find_hypotenuse(length, width):
    hypotn = math.sqrt((length ** 2 + width ** 2))
    return hypotn

def multiply_of(x, y):
    multiplied = x%y
    if multiplied == 0:
        return True
    else:
        return False

def box_of_stars(size):
    starbox = ('*'*size)
    return starbox

def is_even(number):
    even_odd = number%2
    if even_odd != 0:
        return False
    elif even_odd == 0:
        return True

def area_circle(radius):
    circle = math.pi * radius**2
    return circle