class Engine():
    def __init__(self, name, cc):
        self.name = name
        self.capacity = cc

    def start(self):
        print("Started engine")
    def stop(self):
        print("Stopped engine")

class Car:
    def __init__(self, name, cc):
        self.name = name
        self.engine = Engine(name, cc)

    def run(self):
        self.engine.start()
        print("Car is running")

c1 = Car("Audi", 2022)        
c1.run() 

