class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    
class dummy:
    def __init__(self,):
        self.value = 0

    def details(self, std):
        self.value = std



s1 = Student("Akash", 76567)
d1 = dummy()
d1.details(s1) 


d1.details(s1.name)
print(d1.value, s1) 

value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value)