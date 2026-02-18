class Student:
    def __init__(self, *info):
        if len(info) == 3:
            self.name = info[0]
            self.id = info[1]
            self.cgpa = info[2]
            print("Name:", self.name, "ID:", self.id, "CGPA:", self.cgpa)

        elif len(info) == 2:
            self.name = info[0]
            self.id = info[1]
            print("Name:", self.name, "ID:", self.id,)

        elif len(info) == 1:
            self.name = info[0]
            print("Name:", self.name)

        print("Inside def but outside condition")


s1 = Student("sabbir", 22002, 3.11)
s2 = Student("Al-Amin", 23224)
s3 = Student("Tamim")
s4 = Student()