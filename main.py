# 1-misol
class Transport:
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def move(self):
        print(f"Transport {self.speed} tezlik, {self.fuel} yoqilg'i bilan harakatlanmoqda")

class Car(Transport):
    def __init__(self, speed, fuel, brand, color):
        super().__init__(speed, fuel)
        self.brand = brand
        self.color = color

    def move(self):
        super().move()
        print(f"Car {self.brand}, rang: {self.color}")

m1 = Car("BMW", 155, 50, "Oq")
m1.move()

# 2-misol
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"ism: {self.name}")
        print(f"yosh: {self.age}")
        print(f"jinsi: {self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, grade, university):
        super().__init__(name, age, gender)
        self.grade = grade
        self.university = university

    def introduce(self):
        super().introduce()
        print(f"kurs: {self.grade}")
        print(f"university: {self.university}")


s1 = Student("Ali", 15, "Erkak", "2-kurs", "TATU")
s1.introduce()

# 3-misol
class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def eat(self):
        print(f"{self.name}, ovqat yeyapti")


class Dog(Animal):
    def __init__(self, name, age, type, breed, color):
        super().__init__(name, age, type)
        self.breed = breed
        self.color = color

    def eat(self):
        super().eat()
        print(f"tez yeyapti")

    def bark(self):
        print(f"{self.type} hurmoqda")


d1 = Dog("doggy", 2, "it", "kuchuk", "oq")
d1.eat()

# 4-misol
class Employee:
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def work(self):
        print(f"{self.name} ishlamoqda")

class Manager(Employee):
    def __init__(self, name, salary, experience, department, team_size):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.department = department
        self.team_size = team_size

    def work(self):
        super().work()
        print(f"Manager: {self.department} bo'limini boshqarmoqda")


m1 = Manager("Ali", 50000, "Orta", "Menejer", "5-soat")
m1.work()

# 5-misol
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        print(f"Shakl yuzasi aniqlanmagan")

class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self):
        super().area()
        print(f"{self.width * self.height}")

r1 = Rectangle("Kvadrat", "qora", 12, 32)
r1.area()

# 6-misol
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"{self.title} oqilmoqda")

class EBook(Book):
    def __init__(self, title, author, pages, file_size, format):
        super().__init__(title, author, pages)
        self.file_size = file_size
        self.format = format

    def read(self):
        super().read()
        print(f"file_size: {self.file_size}")
        print(f"format: {self.format}")

e1 = EBook("Otkan kunlar", "Abdulla Qodiriy", 223, "4A", "")
e1.read()

# 7-misol
class Device:
    def __init__(self, brand, power, warranty):
        self.brand = brand
        self.power = power
        self.warranty = warranty

    def turn_on(self):
        print(f"{self.brand} yoqildi")

class Phone(Device):
    def __init__(self, brand, power, warranty, model, sim_count):
        super().__init__(brand, power, warranty)
        self.model = model
        self.sim_count = sim_count

    def turn_on(self):
        super().turn_on()
        print(f"model: {self.model}")
        print(f"sim :{self.sim_count}")

p1 = Phone("Iphone", "100%", "", "Iphone 15", 12)
p1.turn_on()

# 8-misol
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self):
        print(f"{self.username} tizimga kirdi")

class Admin(User):
    def __init__(self, username, password, email, role, permissions):
        super().__init__(username, password, email)
        self.role = role
        self.permissions = permissions

    def login(self):
        super().login()
        print(f"role: {self.role}")

a1 = Admin("xxxx", "login45", "login45@gmail.com", "", "")
a1.login()

# 9-misol
class Vehicle:
    def __init__(self, speed, weight, fuel_type):
        self.speed = speed
        self.weight = weight
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.speed} bilan harakat")

class Bike(Vehicle):
    def __init__(self, speed, weight, fuel_type, bike_type, gear):
        super().__init__(speed, weight, fuel_type)
        self.bike_type = bike_type
        self.gear = gear

    def drive(self):
        super().drive()
        print(f"{self.bike_type}")

b1 = Bike(50, 155, "", "sport", "")
b1.drive()

# 10-misol
class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience - experience

    def teach(self):
        print(f"{self.name} dars bermoqda")


class MathTeacher(Teacher):
    def __init__(self, name, subject, experience, level, salary):
        super().__init__(name, subject, experience)
        self.level = level
        self.salary = salary

    def teach(self):
        super().teach()
        print(f"{self.level}")


m1 = MathTeacher("Lola", "math", "", "4-level", 23000)
m1.teach()
