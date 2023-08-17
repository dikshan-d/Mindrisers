# class Vehicle:
    
#     def set_name(self,name):
#         self.name = name
#         self.get_name()
#     def get_name(self):
#         print(self.name)

# car = Vehicle()
# car.set_name('gtr')

# #magic method
# class Car:
#     def __init__(self,name,speed,weight):
#         self.name =name
#         self.speed = speed
#         self.weight = weight
#     def __str__(self):
#         return self.name
# car = Car(name="BMW",speed="200km",weight="120")
# print(car)

# class Bike:
#     def __init__(self,Name):
#         self.name = Name
#         print(self.name)
#     def __str__(self):
#         return self.name
# bike = Bike(Name = "RTR")
# umm = Bike("BMW")

#inheritance
# class Vehicle:
#     def __init__ (self,wheel):
#         self.wheel = wheel
#     def get_wheel(self):
#         pass

# class Car(Vehicle):
#     def get_wheel(self):
#         return self.wheel
# car1 = Car(4)
# print(car1.get_wheel())


#polymorphism
# class Animal:
#     def get(self):
#         print("This is animal")
# class Vehicle:
#     def get(self):
#         print("This is vehicle")
# a1 = Animal()
# v1 = Vehicle()
# a1.get()
# v1.get()

#Encapsulation
class User:
    def __init__ (self,email,password):
        self.__email = email
        self.__password = password
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email
        self.get_email()
    def get_pass(self):
        return self.__password
    def set_pass(self,password):
        self.__password = password
        self.get_pass()

u1 = User("1@gmail.com","1234")
u1.set_email("e@gmail")
print(u1.get_email())
u1.set_pass("1223")
print(u1.get_pass())

# u1.set("D")
# u1.get()

#abstraction
# from abc import abstractclassmethod,ABC
# class Form(ABC):
#     @abstractclassmethod
#     def get(self):
#         print("Hello")
# class Myclass(Form):
#     pass
# f1 = Form()
# # f1.get()
# c1 = Myclass()
# c1.get()

#property

# `def hello(abc):
#     print("hello")
#     abc()
# @hello
# def game():
#     print('Play')
