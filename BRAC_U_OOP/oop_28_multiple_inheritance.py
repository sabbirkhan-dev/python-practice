class A:
    def __init__(self):                   # constructor
        print("init is class A")
    def method1(self):
        print("Method of class A")

class B:
    def __init__(self):
        print("init is class B")
    def method1(self):
        print("Method2 of class B")

# MRO (Method Resolution Order) 
class C(A, B):        # left to right
    def __init__(self):
        super().__init__()
        print("Method of class C Super")

    def method3(self):
        print("Method of class C")

print(C.mro(), "\n") # check MRO 

c1 = C()
c1.method1() 

# B.method1(c1) # c1 


