#learning about functions
#what are functions?
#functions are a block of reusable code that only runs when its called
#you can pass data, known as parameters or arguments, into a function.A function can return data as a result
#functions help to organize and modularize code

#how to define a function
#in python, a function is defined using the "def" keyword
def my_function():
    print("Hello from a function")

#how to call a function
#to call a function, use the function name followed by parenthesis
my_function()

def greetings(user_name):
    return (f"Hello {user_name}")

print(greetings("John"))

# calculate the area of a circle

import math

def circle_area(radius):
    return math.pi * radius **2 #the formula is usualy pi * r^2

print(circle_area(5))

#not using math module
#def circle_area(radius):
 #   return 3.142 * radius ** 2

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height
radius=(int(input("Enter the radius: ")))
height=(int(input("Enter the height: ")))
print(cylinder_volume(radius, height))

def grade_score(score):
    if score >=90:
        return "Qualifies for group A"
    elif score >=90:    
        return "Qualifies for group B"  
    elif score <=70:    
        return "Qualifies for group C"     
    elif score <=60:
        return "Quailifies for group D"
    else:
        score <50
        return "Qualifies for group E"


score=int(input("Enter your score: "))
print(grade_score(score))