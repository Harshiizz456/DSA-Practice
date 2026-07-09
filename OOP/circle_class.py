class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return 3.14* self.radius * self.radius
        
c1 = Circle(2)
print(c1.area())

# Approach 2

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return math.pi * self.radius ** 2

c1 = Circle(2)
print("Area:", c1.area())
