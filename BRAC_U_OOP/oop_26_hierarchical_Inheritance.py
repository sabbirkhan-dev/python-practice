class Student:           # Parent/Super/Base class 
    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):
        print(f"Name: {self.name}, ID: {self.__id}")

# CSE 
class CSE_Student(Student): # If the name inside the brackets is given, it becomes the Parent Class
    def __init__(self, name, Id, lab):
        super().__init__(name, Id)
        self.num_of_lab = lab

    def cry(self):
        print(f"CSE student is crying because of {self.num_of_lab} lab")

# BBA 
class BBA_Student(Student):
    def party(self):
        print(f"BBA student is always partying")

# Object call
c1 = CSE_Student("Sabbir", 25031122, 3) 
c1.details()
c1.cry()
print("---------------------------------")
b1 = BBA_Student("Tuhin", 26024421)
b1.details()
b1.party()
