# Method Resolution Order (MRO) 

class Perant:           # ^
    num = 4

class Child(Perant):     # 1 ^
    num = 5

class Child_2(Child):    # 0 ^
    pass

c1 = Child_2()     # 1 got the num 
print(c1.num)


# Example 2 

class A:
    def a(self):
        return "Function inside A"

class B:
    def a(self):
        return "Function inside B"
    
class C:       # Multiple inheritance A left side class priority 
    def a(self):
      return "Function inside C"
    
class D(A, B):
    def a(self):
        return "Function inside D"
    
class E(B, C):
    def a(self):
        return "Function inside E"

class F(E, D, C):
    pass


# c1 = C()
# print(c1.a()) 

# d1 = D()
# print(d1.a())

f1 = F()
print(f1.a()) 
print(F.mro()) 

