# Print numbers from 1 to 10.
for i in range(1,11):
    print(i)
    
# Display multiplication table for a given number.
num = int(5)
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

# Find factorial of a number.
num = int(5)
f=1
for i in range(1,num+1):
    f=f*i
    print(f)

# Generate the first N Fibonacci numbers.
num = int(10)
a,b = 0,1
for i in range(num):
    print(a)
    a,b =b, a+b

# Check if a number is prime.
num = int(input("Enter a Number:"))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
    
# Reverse a number (e.g., 123 → 321).
num = int(input("Enter number:"))
rev=0
while num>0:
    rev = rev*10 + num%10
    num = num//10
print(rev)

# Count digits in a number.
num = int(input("Enter Number:"))
count = 0
while num > 0:
    count += 1
    num//= 10
print(count)  
  
# Find sum of even numbers between 1–100.
sum = 0
for i in range(1,100):
    if i%2 == 0:
        sum += i
print(sum) 
       
# Print a pyramid pattern.
num = int(input("Enter Number:"))
for i in range(1,num+1):
    print("*" *i)

# Find all divisors of a number.
num = int(input("Enter number:"))
for i in range(1, num+1):
  if num % i == 0: 
      print(i)
        
    