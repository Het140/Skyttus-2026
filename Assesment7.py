# Write a program to handle division by zero error.
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result= a/b
    print("Result=",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
# Write a program to handle invalid integer input.
try:
    num = int(input("Enter an Integer:"))
    print("You Entered:",num)
except ValueError:
    print("Error:Invalid Integer")

# Write a program to open a file and handle the “file not found” error.
try:
    file = open("Assesment4.py","r")
    print(file.read())
    file.close()
except FileNotFoundError:
 print("Error: File not found")

# Write a program to demonstrate multiple exception blocks.
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result = a / b
    print("Result=", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Invalid Integer")

except Exception:
    print("Some other error occurred")

    
# Write a program to use finally for resource cleanup.
try:
    file = open("Assesment4.py","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Closing file")
    try:
        file.close()
    except:
        pass

# Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter Age:"))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Valid Age")
except InvalidAgeError as e:
    print("Error:",e)
    
# Write a program to handle IndexError when accessing a list.
try:
    num = [10,20,30,40]
    index = int(input("Enter Index:"))
    print("Value:", num[index])
except IndexError:
    print("Error: Index out of Range")
    
# Write a program that takes two numbers and handles all possible errors.
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result= a/b
    print("Result=",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error:Invalid Integer")
except Exception:
    print("Some other error occurred")
finally:
    print("Program executed")

# Write a program to log errors to a file instead of printing them.
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result= a/b
    print("Result=",result)
except Exception as e:
    file = open("Assesment4.py","a")
    file.write(str(e)+"\n")
    file.close()

# Write a program that validates an email format and raises an exception for invalid ones.	
class InvalidEmailError(Exception):
    pass
try:
    email = input("Enter Email:")
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid Email Format")
    print("Valid email")
except InvalidEmailError as e:
    print("Error:",e)