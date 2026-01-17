# Create a custom math module and import it in another file.
# def add(a,b):
#     return a + b
# def subtract(a,b):
#     return a - b
# def multiply(a,b):
#     return a * b
# def divide(a,b):
#     if b !=0:
#         return a / b
#     return "Cannot divide by zero"
 
# Create a module to perform string operations. 
# def to_upper(text):
#     return text.upper()
# def to_lower(text):
#     return text.lower()
# def reverse_string(text):
#     return text[::-1]
# def count_character(text):
#     return len(text)
# def replace_space(text):
#     return text.replace(" ","_")

# Use random module to generate 5 random integers. 
# import random
# for i in range(5):
#     print(random.randint(1,100))
    
# Use datetime module to display current date and time.
# from datetime import datetime 
# now = datetime.now()
# print("Current Date and Time:", now)

# Use math module to find factorial of a number.
# import math
# num = 5
# result = math.factorial(num)
# print("Factorial of", num, "is", result)

# Create a package shapes with modules for circle and rectangle. 
# import math
# def area(radius):
#     return math.pi*radius*radius
# def perimeter(radius):
#     return 2*math.pi*radius
# def area1(length, width):
#     return length * width
# def perimeter1(length,width):
#     return 2*(length + width)

# Import multiple functions from one module and use them. 
# def add(a,b):
#     return a + b
# def subtract(a,b):
#     return a - b
# def multiply(a,b):
#     return a * b

# Write a program to shuffle a list using random module. 
# import random
# number = [1,2,3,4,5]
# random.shuffle(number)
# print("Shuffled list", number)

# Write a program to calculate the difference between two dates. 
# from datetime import date
# date1 = date(2024,12,1)
# date2 = date(2025,12,12)
# difference = date2-date1
# print("Difference in days:", difference.days)

# Use os module to list files in a directory.	
import os
path = "."
files = os.listdir(path)
print("Files in Directory:")
for file in files:
    print(file)