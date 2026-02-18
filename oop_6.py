class Cat:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def display(self, num, clr):
        num = num + 5
        clr1 = clr              #.copy()   
        clr1[0] = "Green"
        print("Instand", num)
        print("Instand", clr1)



colors = ["Black", "Red", "Yellow", "Blue"]
num_1 = 55

c1 = Cat("White", "Jumping")
c1.display(num_1, colors)

print(colors,num_1)

