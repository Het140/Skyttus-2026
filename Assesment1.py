# Write a program to print your name, age, and city in one line

name = "Het Patel"
age = "21"
city = "valsad"

print(name,age,city)

# Take user input for two numbers and pint their sum

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

sum = num1 + num2
print("Sum =", sum)

# Write a program to covert temperature from celcius to feranhite

celsius = float(input("Enter temperature in celcius:"))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

# Store your name in a variable and print it in uppercast

name = "Het Patel"
print(name.upper())

# Ask the user for their birth year and calculate their current age

birth_year = int(input("Enter your birth year:"))
current_year = 2026

age = current_year - birth_year
print("Your age is:", age)

# Write a program to swap the value of two variable

a = int(input("Enter first number:"))
b = int(input("Enter second number"))

temp = a
a = b
b = temp

print("After swapping")
print("a =", a)
print("b =", b)

# Create a program to calculate the area of a rectangle from the user inputs.

length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

area = length * width
print("Area of the rectangle =", area)

# Write a program to check if a number is positive or negative.

num = int(input("Enter the number:"))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")  
    
# Ask for two numbers and print their average.
 
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

average = (num1 + num2)/2
print("Average =",average)