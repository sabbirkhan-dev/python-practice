class Student:
    def __init__(self, name , ID):
        self.name = name      # pubilc variable
        self.__ID = ID        # privet variable

    def details(self):
        return f"Name: {self.name}, ID: {self.__ID}"
    
    def update_id(self, ID):
        if ID > 0:
            self.__ID = ID
        else:
            print("Invaild ID, Try again later")


s1 = Student("Amir", 1122)
print(s1.details())

s2 = Student("Hamza", 9900)
s2.update_id(8811)
print(s2.details()) 

