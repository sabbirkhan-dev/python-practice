# Python OOP | Inheritance | Method Overriding
class A:
    def __init__(self):
        print("__init__ class A")
    def method1(self):
        print("Sometime study")

    def method2(self):
        print("You will get all of properties and method")

class B(A):
    # def __init__(self):
    #     super().__init__()
    # def method1(self):
    #     print("Always party")
    #     return super().method1()

    def method1(self):
        super().method1()
        print("Always party") 
    
b1 = B()
b1.method1()
b1.method2()