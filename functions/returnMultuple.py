import math
def circle_status (radius):
    area = math.pi*radius**2
    circumferacne = 2*math.pi*radius
    return area , circumferacne




a,c = circle_status(6)
print("Area of circle", a, "Circumferacne of circle",c)