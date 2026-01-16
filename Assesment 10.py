# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
# class car:
#     def __init__(self, brand, model,speed):
#      self.brand = brand 
#      self.model = model
#      self.speed = speed
     
#     def accelerate(self, increase):
#         self.speed += increase
#         print(f" Car accleration .Current speed: {self.speed} km/h")  
        
#     def brake(self, decrease):
#         self.speed -= decrease
#         print(f" Car decelerate . Current speed: {self.speed} km/h")
                
# my_car = car("Honda","Defender",50)
# my_car.accelerate(20)
# my_car.brake(15) 
             
# Create a BankAccount class with deposit and withdraw methods. 
# class BankAccount:
#     def __init__(self,account_holder,balance=0):
#      self.account_holder = account_holder
#      self.balance = balance
     
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#         print("Current Balance:", self.balance)
#     def withdraw(self, amount):
#         if amount <+ self.balance:
#             self.balance -= amount
#             print("Deposited:", amount)
#             print("Current Balance:", self.balance)  
#         else:
#             print("Insufficient balance")   
            
# acc = BankAccount("Het Patel", 10000) 
# acc.deposit(1000)
# acc.withdraw(3000)
           
# Create a Student class with a method to calculate average marks. 
# class Student:
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks
#     def calculate_average(self):
#         total = sum(self.marks)
#         average = total/ len(self.marks)
#         return average
        
# student1 = Student("Het",[80,90,95,88])
# print("Average Marks:", student1.calculate_average())      
# Create a Rectangle class with methods to find area and perimeter. 
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width 
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return 2*(self.length + self.width)
    
# rect1 = Rectangle(20,8)
# print("Area:", rect1.area())
# print("Perimeter:",rect1.perimeter())    
        
# Create an Employee class that displays salary details. 
# class Employee:
#     def __init__(self,emp_id, name, Salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.Salary = Salary
#     def display_salary(self):
#         print("Employee ID:",self.emp_id)
#         print("Employee Name:",self.name)
#         print("Salary:",self.Salary)
        
# emp = Employee(90,"Het Patel",60000)
# emp.display_salary()    
        
# Create a Book class to store title, author, and price, and display details. 
# class Book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
        
#     def display_details(self):
#      print("Title:", self.title)
#      print("Author:",self.author) 
#      print("Price:",self.price) 
     
# book = Book("Harry Potter and the deadly hallows Part 1","J.K Rowling","12,999")      
# book.display_details() 

# Create a Circle class to find area and circumference. 
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius*self.radius
#     def circumference(self):
#         return 2* 3.14* self.radius
    
# circle = Circle(5)
# print("Area",circle.area())
# print("Circumference:" ,circle.circumference())
    
# Create a Laptop class with a method to apply discounts on price.
# class Laptop:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#     def apply_discount(self,discount_percent):
#         discount_amount = (discount_percent/100)* self.price
#         self.price = self.price - discount_amount
#         print("Brand:", self.brand)
#         print("Print after discount:", self.price)
        
# laptop = Laptop("Dell", 50000)   
# laptop.apply_discount(15)   
      
# Create a Flight class with seat booking functionality. 
# class Flight:
#     def __init__(self, flight_no, total_seats):
#         self.flight_no = flight_no
#         self.total_seats = total_seats
#         self.booked_seats = 0
#     def book_seat(self, seats):
#         if self.booked_seats + seats <= self.total_seats:
#            self.booked_seats += seats
#            print(seats, "seat(s) booked successfully")
#         else:
#             print("Not enough seats available")
#     def available_seats(self):
#         return self.total_seats - self.booked_seats
    
# flight1 = Flight("AI201",100) 
# flight1.book_seat(50)  
# print("Available seats:" ,flight1.available_seats())   
          
# Create a Shop class with a method to add and list products.	
class Shop:
    def __init__(self,shop_name):
        self.shop_name = shop_name
        self.product = []
    def add_product(self,product):
        self.product.append(product)
        print(product,"added to shop")
    def list_product(self):
        print("Product available in" ,self.shop_name)
        for product in self.product:
            print("-",product)
            
shop = Shop("D-Mart")
shop.add_product("Milk")
shop.add_product("Sugar")
shop.add_product("Rice")
shop.add_product("Stationary")             
shop.list_product()       