import math
def circle_area(radius):
    return math.pi * radius ** 2
print(circle_area(23))

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height
radius=int(input("Enter the radius: "))
height=int(input("Enter the height: "))
print(cylinder_volume(radius, height))
