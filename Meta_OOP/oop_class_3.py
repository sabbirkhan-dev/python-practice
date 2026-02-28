class recipe:
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def content(self):
        print(f"The {self.dish} has {self.items} \nand take time {self.time} min to prepare")

pizza = recipe("Pizza", ["cheese", "Bread", "Tomato"], 45)
pasta = recipe("Pasta", ["penne", "souce"], 65)

pizza.items
pizza.content()

pasta.content()


print("ju", pizza.content())





class Test:

    x = 5

t1 = Test()
t2 = Test()

t1.x = 10

print(t1.x)
