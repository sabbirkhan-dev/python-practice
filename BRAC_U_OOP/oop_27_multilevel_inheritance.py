# Multilevel Inheritance
class Student:           # Parent/Super/Base class 
    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):
        print(f"Name: {self.name}, ID: {self.__id}")

# CSE 
# If the name inside the brackets is given, it becomes the Parent Class
class CSE_Student(Student):         # Child
    def __init__(self, name, Id, lab):
        super().__init__(name, Id)
        self.num_of_lab = lab

    def cry(self):
        print(f"{self.name} is a CSE student and he is crying because of {self.num_of_lab} labs")

class CSE_Fresher(CSE_Student):         # Grandchild
    def enroll_CSE_111(self):
        print(f"{self.name} Enrool in CSE 111")

# object call
s1 = CSE_Student("Sumon", 11034499, 3)
s1.details()
s1.cry()
print("---------------------------------------------------------------------")
f1 = CSE_Fresher("Rana", 26036464, 3)
f1.details()
f1.enroll_CSE_111()
f1.cry()
