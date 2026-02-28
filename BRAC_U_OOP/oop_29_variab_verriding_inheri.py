class Animal:
    def __init__(self, name):
        self.name = name
        self.color = "White"

    def eat(self):
        print(f"{self.color} {self.name} is eating")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print(f"{self.color} {self.name} is meowing")


c1 = Cat("cat", "brown")
c1.meow()
c1.eat()
