class Student:
    uni_name = "DU"     
    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def datials(self):
        print(f"Name: {self.name}, ID: {self.__id}, University: {Student.uni_name}")

    @classmethod
    def up_uni_name_cls(cls, up_u_name):
        cls.uni_name = up_u_name    

    @classmethod
    def from_str(cls, info):
        name, id = info.split("-")  
        get_obj = cls(name, id)
        return get_obj


s1 = Student("Rajib", 121)
s2 = Student("Rakib", 223)
s1.datials()
s2.datials()

Student.up_uni_name_cls("NU")        # call classmethod 
s3 = Student("Sozib", 444)
s3.datials() 

s4 = Student.from_str("Amin-1122") 
s4.datials() 

