# Create a base class Animal and subclasses Dog and Cat. 
# class Animal:
#     def __init__(self,name):
#      self.name = name
#     def speak(self):
#         print("The sound animal makes")
        
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} Says: Woof!")
# class cat(Animal):
#     def speak(self):
#         print(f"{self.name} Says: Meow!")

# dog = Dog("Buddy")
# cat= cat("Micky")
# dog.speak()
# cat.speak()  
                   
# Create a class hierarchy for Vehicle → Car → ElectricCar. 
# class Vehicle:
#     def start(self):
#         print("Vehicle started")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is Driving")
# class ElectricCar(Car):
#     def charge(self):
#         print("Electric car is charging")
        
# ec = ElectricCar()
# ec.start()
# ec.drive()
# ec.charge()             
           
# Implement method overriding in a base and derived class. 
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed    
#     def sound(self):
#         print(f"{self.name} the {self.breed} barks")
        
# dog = Dog("Charlie","Labrador")
# dog.sound()                    
              
# Demonstrate multiple inheritance with two parent classes.
# class Teacher:
#     def __init__(self,name):
#         self.name = name
# class Subject:
#     def __init__(self,subject):
#         self.subject = subject 
# class Faculty(Teacher, Subject):
#     def __init__(self, name, subject):
#         Teacher.__init__(self,name)
#         Subject.__init__(self, subject) 
#     def show(self):
#         print(self.name, "teaches", self.subject)
        
# f = Faculty("Het", "Python")    
# f.show()            
 
# Create a polymorphic function that works with different shapes. 
# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length*self.width
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14* self.radius*self.radius
    
# def print_area(shape):
#         print("Area:",shape.area())
        
# r = Rectangle(5,4)
# c = Circle(3)
# print_area(r)
# print_area(c)       
                 
# Create a Bank system with SavingsAccount and CurrentAccount classes. 
# class BankAccount:
#     def __init__(self, account_number, holder_name,balance=0):
#         self.account_number= account_number
#         self.holder_name = holder_name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Deposite {amount}. New balance: {self.balance}")
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -=amount
#             print(f"Withdraw {amount}.New balance:{self.balance}")
            
#     def show_balance(self):
#         print(f"Account:{ self.account_number}, Holder: {self.holder_name},Balance: {self.balance}")
# class SavingAccount(BankAccount):
#     def __init__(self,account_number,holder_name, balance=0, interest_rate=0.04):
#         super().__init__(account_number,holder_name,balance)
#         self.interest_rate= interest_rate
        
#     def add_interest(self):
#         interest = self.balance*self.interest_rate
#         print(f"Interest added: {interest}. New balance: {self.balance}")
  
# class currentAccount(BankAccount):
#     def __init__(self,account_number,holder_name,balance=0,overdraft_limit=5000):
#         super().__init__(account_number,holder_name,balance) 
#         self.overdraft_limit = overdraft_limit
#     def withdraw(self,amount):
#         if amount > self.balance + self.overdraft_limit:
#             print("Exeeded overdraft limit!")
#         else:
#             self.balance -= amount
#             print(f"Withdraw {amount}. New balance: {self.balance}")
            
# savings = SavingAccount(101,"Het",3000) 
# current = currentAccount(102,"Jay",2000)
# savings.deposit(500)
# savings.add_interest()
# savings.withdraw(300)
# savings.show_balance()

# current.deposit(1000)
# current.withdraw(3500)
# current.withdraw(5000)
# current.show_balance()                                
                        
# Create a class with private attributes and getter/setter methods.
# class Person:
#     def __init__(self,name,age):
#         self.__name = name 
#         self.__age = age
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name = name
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         if age> 0:
#             self.__age = age
#         else:
#             print("Invalid age!")

# p = Person("Het", 21)
# print(p.get_name())
# print(p.get_age())
# p.set_name("Bob")
# p.set_age(30)
# print(p.get_name())
# print(p.get_age())
# p.set_age(-5)   
                 
# Create a Teacher and Student class to show inheritance.
# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
#     def teach(self):
#         print(f"{self.name} is teaching {self.subject}")
# class Student(Teacher):
#     def __init__(self, name, subject, student_name):
#         super().__init__(name,subject)
#         self.student_name = student_name
#     def study(self):
#         print(f"{self.student_name} is studying {self.subject}")
        
# t = Teacher("Mr.Patel","Python")
# s = Student("Mr.Dave","Maths","Amit")

# t.teach()
# s.teach()
# s.study()
               
# Create a MusicPlayer class and subclass Spotify to override play method.
# class MusicPLayer:
#     def __init__(self,song):
#      self.song = song 
#     def play(self):
#         print(f"Playing {self.song} on generic music player")
# class Spotify(MusicPLayer):
#     def play(self):
#         print(f"Streaming {self.song} on Spotify")
        
# player = MusicPLayer("Shape of you")
# spotify_player = Spotify("Blinking Light")
# player.play()
# spotify_player.play()         
        
# Demonstrate the use of super() in inheritance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
    def show(self):
        super().show()
        print(f"Employee ID: {self.employee_id}") 
        
e = Employee("Het",21,103)
e.show()                 	