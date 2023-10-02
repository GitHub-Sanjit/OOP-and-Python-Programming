"""
Inheritance:
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class (subclass or derived class) by inheriting properties and behaviors (attributes and methods) from an existing class (base class or superclass). The derived class can extend or override the functionalities of the base class.

Example:
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"
