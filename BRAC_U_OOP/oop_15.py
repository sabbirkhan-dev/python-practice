class Student:
    def __init__(self, name, id):
        self.name = name       # instance variable
        self.__id = id          # privet instance variable

    def details(self):
        print(f"Name: {self.name} ID: {self.__id}")
        self.__method()

    def __method(self):      # Private method 
        print("Privet method executed")

s1 = Student("Jahid", 1122)
s1.details()
        