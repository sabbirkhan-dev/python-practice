class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def Move(self):
        print("Move!")

class Car(Vehicle):
    def Move(self):
        print("Car is running on the road")

class Boat(Vehicle):
    pass

class Plane(Vehicle):
    def Move(self):
        print("The plane is flying in the sky")


# p1 = Plane("BMW", 2003) 
# p1.Move()
c1 = Car("Toyato", "Corolla")
p1 = Plane("JetBlue", 707)

for x in [c1, p1]:
    print(x.brand)
    x.Move()

