class Student:
    count = 0   #  Class or Static variable 
    def __init__(self, name, id):
        self.name = name   # instance variable
        self.id = id
        Student.count += 1

    def details(self):
        print(f"Name: {self.name}, ID: {self.id}, Total student count: {Student.count}")


s1 = Student("Apu", 11)
s2 = Student("Amin", 22)
s3 = Student("Shovon", 33)
s4 = Student("Majeda", 44)
print(Student.count) 

