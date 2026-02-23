class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def viwe(self):
        return f"This house has window {self.window} and door {self.door}"

    def __add__(self, other):
        new_w = self.window + other.window
        new_d = self.door + other.door
        obj = House(new_w, new_d)
        return obj
    

h1 = House(2,4)
print(h1.viwe())

h2 = House(10, 5)
h3 = h1 + h2          # d + w 
print(h3.viwe())  

print(h3.door)   # output door 

