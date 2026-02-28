class Student:
    uni_name = "UIU"
    def __init__(self, name, id):
        self.name = name
        self.__id = str(id)
        Student.check_department(self.__id)

    def details(self):
        print(f"Name: {self.name}, ID: {self.__id}, UNIV: {Student.uni_name}")

    @classmethod
    def up_uni_name(cls, up_u_name):
        cls.uni_name = up_u_name

    @staticmethod
    def check_department(id):
        if id [2:4] == "01" : print("Department CSE")
        elif id [3:5] == "41" : print("Department BBA")

# call obj

s2 = Student("Sakib", 25041146)
s2.details() 

print("--------------------------------------")

s1 = Student("Tuhin", "25041146")   
s1.details()

