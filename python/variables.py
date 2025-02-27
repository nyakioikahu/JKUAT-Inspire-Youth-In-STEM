dog_name = "German" # string
dog_second_name = 'Shepherd' # string
dog_fur_color = "brown" # string
dog_age = 7 #integer
dog_height = 2.5 #float
#print(dog_name)
# Operators in python
#1. Arithmetic operators
num1=20
num2=40
addition = num1 + num2
#print(addition) 
subtraction = num1 - num2
#print (subtraction)
multiplication = num1 * num2
#2. Comparison operators
#print(num1 == num2)
#print(num1>num2)
#print(num1!=num2) #true
#3. Logical operators
# and, or, not
#print(num1<num2 and num1>num2) #false
#print(num1<num2 or num1>num2) #true
#print(not num1<num2) #false
#4. Assignment operators
#num1 +=2
#print(num1)
#num1 *=2
#print(num1)
#5. Identity operators
# is, is not
#print(num1 is not num2) #true

#6. Conditional statements
# if, elif, else

if dog_age >= 5:
    print("old dog")
    
enter_name = input("Enter your name: ")    
enter_age = int(input("Enter your age: "))
if enter_age <= 18:
    print("You are a child!")
if enter_age >= 18:
    print("You are an adult!")

