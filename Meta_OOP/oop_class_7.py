# multi level inheritance

class A:
    a = 1
    
class B(A):
    a = 277
    
class C(B):
    pass

c = C()
print(c.a) 


# is sub class

class A:
    pass
class B(A):
    pass

a = B()
print(issubclass(B,A))


# isinstance()

class C:
    pass
class D(C):
    pass
c = D()
print(isinstance(c, D)) 
print(isinstance(c, C)) 


# super() function 
class Fruit:
    def __init__(self, fruit):
        print(fruit)

class Apple(Fruit):
    def __init__(self):
        super().__init__("Apple") 
        print("Sweet")

a = Apple()


# Here is an example. 

class Fruits:
    def __init__(self, fruits):
        print("Fruits type", fruits)

class Fruits_falaver(Fruits):
    def __init__(self):
        super().__init__("Mango")
        print("This fruits is sweet")

f = Fruits_falaver()


class Fruit_2:
    def __init__(self, fruit2):
        print("Fruits type", fruit2)

class Fruit2_falaver(Fruits):
    def __init__(self, *fruit2):
        super().__init__(fruit2)    
        print("This fruits is sweet")

f = Fruit2_falaver("Orange", "Apple", "Banana")

