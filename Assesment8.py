# Function to check if a number is prime.
def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1 
            if count == 2:
                return True
            else:
                return False
            
num =int(input("Enter Number:"))
if is_prime(num):
     print("Prime Number")
else:
   print("Not a prime number")
   
# Function to reverse a string.
def reverse_string(s):
    return s[::-1]

text = input("Enter a String:")
print("Reversed String:", reverse_string(text))

# Function to find factorial.
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
        return result
    
num = int(input("Enter a number:"))
print("Factorial:",factorial(num))
    
# Function to calculate simple interest.
def simple_interest(principle, rate, time):
    si = (principle *rate *time)/100
    return si

p = float(input("Enter Principle Amount:"))
r = float(input("Enter Rate of Interest:"))
t = float(input("Enter time in year:"))
print("simple Interest=",simple_interest(p,r,t))

# Function to check if a word is palindrome.
def is_palindrom(word):
    word = word.lower()
    return word == word[::-1]

text = input("Enter a Word:")
if is_palindrom(text):
    print("Palindrome")
else:
    print("Not a Palindrome")
    
# Function to count vowels in a string.
def count_vowels(s):
    vowel = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
            return count
        
text = input("Enter a string:")
print("Number of Vowels:", count_vowels(text))   
     
# Function to merge two lists.
def merge_lists(list1,list2):
    return list1 + list2

list1 = [1,2,3]
list2 = [4,5,6]
merged = merge_lists(list1,list2)
print("Mergerd list:",merged)

# Function to find GCD of two numbers.
def gcd(a,b):
    while b !=0:
        a, b = b, a % b
    return a
    
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("GCD:", gcd(num1, num2))    

# Function to find area of rectangle.
def area_of_rectangle(length, width):
    return length * width
l = float(input("Enter length:"))
w = float(input("Enter width:"))
print("Area of rectangle:", area_of_rectangle(l,w))

# Function to check Armstrong number.
def is_armstrong(num):
    digits = len(str(num))
    temp = num
    total = 0	
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
        return total == num
    
n = int(input("Enter a number:"))
if is_armstrong(n):
    print("Armstrong Nmumber")
else:
    print("Not an Armstrong number")    