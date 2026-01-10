# Calculate the reminder of two number.

a = 57
b = 2
reminder = a%b
print(reminder)

# Check if the number is even or odd.

num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")    
    
# Compare two number nad print the largest number.

a = 21
b = 22

if a > b:
    print("Larger number:",a)
elif a < b:
    print("Larger number:",b)  
else:
    print("Number is Equal")      

# Write a program to calculate the square and cube of a number.

num = int(input("Enter the Number:"))

Square = num**2
Cube = num**3
print("Square:", Square)
print("Cube:", Cube)

# Check if two entered numbers are equal.

a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))

if a == b:
    print("Number is Equal")
else:
    print("Number is not Equal")  
    
# Take two Nmbers and print true if both are positive, else False. 

a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number"))  

if a > 0 and b > 0:
    print("True")
else:
    print("False")
           
# Write a program to convert Float to Integer. 

num = float(input("Enter a Float Number:"))
int_num = int(num)
print("Integer value:", int_num)          

# Take a number as string, convert to integer and multiply by 10.

num_str = input("Enter a Number:")
num_int = int(num_str)
result = num_int * 10
print("result",result)

# Write a program that uses and & OR operator to check multiple conditions.

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
# Using AND Operator
if a > 0 and b > 0:
    print("Both are Positive")
else:
    print("Both are negative")
# Using OR Operator
if a > 0 or b > 0:
    print("Atleast one Positive")
else:
    print("Neither is Positive")
    
# Divide two Numbers and print the quotient and reminder seperately.

a = int(input("Enter the First Number"))
b = int(input("Enter the Second Number"))
quotient = a//b
reminder = a%b
print("quotient:",quotient)
print("reminder:",reminder)
