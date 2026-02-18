class car:
    def __init__(self, name, modal = 2010):
        self.name = name 
        self.modal_year = modal
        self.wheel = 4

    def viwe(self):
        print(f"This is your car name: {self.name} and modal: {self.modal_year}")
        print(f"This is your wheel: {self.wheel}")

c1 = car("BMW", 2008)
c2 = car("Audi")

c1.viwe()
c2.viwe()