# multi level inheritance

class A:
    a = 1
    
class B(A):
    a = 277
    
class C(B):
    pass

c = C()
print(c.a) 
