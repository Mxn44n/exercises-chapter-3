from math import sqrt

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, p):
        return (sqrt((self.centre[0]-p[0])**2+(self.centre[1]-p[1])**2) <= self.radius)