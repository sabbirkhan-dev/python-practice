class PaySlips:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount

    # payment update function
    def pay(self):
        self.payment = "yes"

    # status check function
    def status(self):
        if self.payment == "yes":
            return f"{self.name} is paid {self.amount}" 
        else:
            return f"{self.name} is not paid yet"


# object create
nathan = PaySlips("Nathan", "no", 1000)
roger = PaySlips("Roger", "no", 3000)

# before payment
print(nathan.status())
print(roger.status())

# pay Nathan
nathan.pay()
print("\nAfter payment:\n")

# after payment
print(nathan.status())
print(roger.status())


