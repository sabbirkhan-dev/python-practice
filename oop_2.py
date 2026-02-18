class computer:
    brand = "Apple"
    def __init__ (self, name, id):
        self.name = name
        self.id = id
    def hello(self):
        print(f"Hello {self.name} from computer. ID: {self.id}")

c1 = computer("sabbir",11)
c1.hello()

print(c1.name)
print(c1.id)

class Student:
    def __init__(self, nm, iD):
        nm = "Surprise!"  
        self.name = nm    
        self.Id = iD

s1 = Student("Pranto", 1)
print(s1.nm, s1.Id)
