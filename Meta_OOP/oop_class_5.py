class employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last


class supervisor(employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class chefs(employees):
    def leave_requst(self, days):
        return f"May I take a leave for {days} days"
    


Karim = chefs("Krim", "Sikder")
print(Karim.leave_requst(8))

Rahim = supervisor("Rahim", "Khan", 998)
print(f"Chefs Name: {Rahim.name}") 
print(f"Password: {Rahim.password}") 


