class Fruit:
    def __init__(self, count):
        print("------Inside class Fruit------")
        self.count = count
    print("print inside fruit class")

    def one_add(self):
        return self.count + 1
    
print(dir(Fruit))
print("Instantiating Fruit..")
fruit_obj = Fruit(77)
print(fruit_obj.one_add()) 

class Basket():
    def __init__(self, fruit_obj):
        print("---Inside class Basket---")
        self.fruit_obj = fruit_obj

        print(fruit_obj.one_add())
        fixed_value = 5
        print(fixed_value)
        print(fruit_obj)

print("Instantiating Basket..")
basket_obj = Basket(fruit_obj)
print(fruit_obj) 


# Composition 

class Engine:
    def start(self):
        return "Engine Start"

class Car:
    def __init__(self, engine):
        self.engine = engine

e1 = Engine()
c1 = Car(e1) 

# print(type(e1))
# print(type(c1))

print(c1.engine.start()) 
print(c1.engine == e1) 




