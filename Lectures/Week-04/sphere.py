from math import pi

def surface_area(radius):
    '''
    Calculate surface area of a sphere
    '''
    return 4 * pi * radius**2

def volume(radius):
    print('calculating volume')
    return (4/3) * pi * radius**3

def circumference(radius):
    return 2 * pi * radius
