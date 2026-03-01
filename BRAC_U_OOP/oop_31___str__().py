class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # print(self) 

    def __str__(self):
        return "This is CSE_111 Course"

e1 = Employee("Amin", 22020367)
print(e1) 


