class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is Barking")

a1 = Animal("Jack")
d1 = Dog("Tom")
d1.bark()

a1.eat()