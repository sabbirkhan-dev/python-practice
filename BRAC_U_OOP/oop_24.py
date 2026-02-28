# Single inheritance
"""class Parent:
    def method1(self):
        print("This is parent class 1")
    def method2(self):
        print("This is parent class 2")

class Child(Parent):
    def method3(self):
        print("This is child clss 3")

c1 = Child()
c1.method1()
c1.method2()
c1.method3()"""


# Multilevel Inheritance
"""
class Parent:
    def method1(self):
        print("This is parent class 1")
    def method2(self):
        print("This is parent class 2")

class Child1(Parent):
    def method3(self):
        print("This is child clss 3")

class Child2(Child1):
    def method4(self):
        print("This is child clss 4")

c1 = Child2()
c1.method1()
c1.method2()
c1.method3()
c1.method4()
"""

# Hierarchical Inheritance 
# to child use 1 parent class
"""class Parent:
    def method1(self):
        print("This is parent class 1")
    def method2(self):
        print("This is parent class 2")

class Child1(Parent):
    def method3(self):
        print("This is child clss 3")

class Child2(Parent):
    def method4(self):
        print("This is child clss 4")

c1 = Child2()
c1.method1()
c1.method2()
c1.method4()
"""

# Hybrid Inheritance

class Parent:
    def method1(self):
        print("This is parent class 1")
    def method2(self):
        print("This is parent class 2")

class Child1(Parent):
    def method3(self):
        print("This is child clss 3")

class Child2(Child1):
    def method4(self):
        print("This is child clss 4")

class Child3(Child1):
    def method5(self):
        print("This is child clss 5") 

c5 = Child3()
c5.method5()
c5.method3() 
