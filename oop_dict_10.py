class Student:

    def __init__(self, **info):
        if len(info) == 3:
            self.name = info["name"]
            self.id = info["id"]
            self.cgpa = info["cgpa"]
            print("Name:", self.name,"\nID:", self.id,"\nCGPA:", self.cgpa)

        elif len(info) == 2:
            self.name = info["name"]
            self.id = info["id"]
            print("Name:", self.name,"\nID:", self.id)

        elif len(info) == 1:
            self.name = info["name"]
            print("Name:", self.name)
        


s1 = Student(name = "Maruf", id = 23113, cgpa = 3.33)
s2 = Student(id = 23113, name = "Shovon")
s3 = Student(name = "Amir") 

