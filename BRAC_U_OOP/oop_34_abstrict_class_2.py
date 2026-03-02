from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")


class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")

class Cow(Animal):
    def make_sound(self):
        print("Caw is mooing")
d1 = Dog()
d1.make_sound()

c1 = Cat()
c1.make_sound()

co = Cow()
co.make_sound()

