class house:
    def __init__(self, window, door=2):  # Default Arguments door = 2
        self.window = window
        self.door = door

    def viwe(self):
        print(f"Our house window {self.window} , door {self.door}")

h1 = house(33,10)
h2 = house(10,2)
print(h1)           # <_main__.house object at 0x0000024637CC86E0>

print(h1.door)
h2.viwe() 