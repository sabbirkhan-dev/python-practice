class Fruit:
    def __init__(self, fruit):
        print("Fruit", fruit)

class Apple(Fruit):
    def __init__(self):
        super().__init__("Apple")
        print("Sweet")

a = Apple() 


# Multiple inheritance

class A:
    a = "a",1
    pass

class B:
    b = "b",1

class C(A,B):
    pass

c = C()
print(c.a, c.b) 