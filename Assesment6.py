# Check if a person is eligible to vote (age ≥ 18).
# age = int(input("Enter the Age:"))
# if age >= 18:
#     print("Eligible to Vote")
# else:
#     print("Not Eligible to Vote")
    
# Grade calculator based on marks: 90+ = A, 80+ = B, else C.
# marks = int(input("Enter your Marks:"))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# else:
#     print("Grade C")
    
# Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
# signal = input("Enter the signal color:")
# if signal == "Red":
#     print("Stop")
# elif signal == "Yellow":
#     print("Wait")
# elif signal == "Green":
#     print("Go")
# else:
#     print("Invalid Color")
    
# ATM withdrawal check: sufficient balance or not.
# balance = 10000
# amount = int(input("Enter the amount to withdraw:"))
# if amount <= 10000:
#     print("Withdraw Succesfull")
# else:
#     print("Insufficient balance")
    
# Check if a number is positive, negative, or zero.
# num = int(input("Enter the Number:"))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
    
# Check if a number lies within a given range.
# num = int(input("Enter a Number:"))
# if num >=1 and num <= 10:
#     print("Number is in Range")
# else:
#     print("Number is not in Range")

# Username & password verification.
# username = input("Enter Username:")
# password = input("Enter password:")
# if username == "Het" and password == "123456":
#     print("Login Succesfull")
# else:
#     print("Invalid Username and Password")
# Electricity bill calculator based on units consumed.
# unit = int(input("Enter units:"))
# if unit <= 100:
#     bill = unit *2
# elif unit <= 200:
#     bill = unit *3
# else:
#     bill = unit *5
#     print("Bill Amount:", bill)

# Simple calculator (add, subtract, multiply, divide).
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number"))
# op = input("Enter the operators(+ - / *):")
# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "/":
#     print(a / b)
# elif op == "*":
#     print(a * b)
# else:
#     print("Default")
    
# Check type of triangle (equilateral, isosceles, scalene).
a = int(input("Enter side 1:"))
b = int(input("Enter side 2:"))
c = int(input("Enter side 3:"))  

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")      