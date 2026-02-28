class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def display(self):
        print(f"Cat name {self.name} color {self.color}")

c1 = Cat("Leo", "Blue")
c1.display()

c1.update_color("red")
c1.display()