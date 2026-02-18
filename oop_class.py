"""class car:
    def __init__(self,brand,modal):
        self.brand = brand
        self.modal = modal
    def __str__(self):
        return(f"car infor {self.brand} & {self.modal}") 

    def show(self):
        print(f"This is your car {self.brand} and modal {self.modal}")

car1 = car(brand="Toyato", modal="Cololla")
print(car1) 
car1.show()

car2 = car(brand="BMW", modal="IX3")
print(car2)
car2.show()
"""
# import keyword
# print(keyword.iskeyword("del"))  * check keyword * 

"""class Car:
    def __init__(self, current_year, manufacturing_year):
        self.current_year = current_year
        self.manufacturing_year = manufacturing_year

    def age(self):
        return self.current_year - self.manufacturing_year 
    
car_1 = Car(2026,2025)
print(car_1.age()) 

garage = [
    Car(2026, 2020),
    Car(2026, 2015),
    Car(2026, 2026)
]

for gari in garage:
    print(gari.age())
"""

class Student:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    def display(self, preprefix = ""):
        print(f"{preprefix}This is a student name: {self.name} & id no: {self.Id}")

s1 = Student("Sabbir", 111)
s2 = Student("Tuhin", 222)

s1.display()
s2.display()
s1.display("2nd ")


