class paysliph:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment.lower()
        self.amount = amount

    # update payment
    def pay(self):
        self.payment = "yes"

    # status check
    def status(self):
        if self.payment == "yes":
            return f"{self.name} is paid {self.amount}"
        else:
            return f"{self.name} is not paid yet"
        
# create object 
rakib = paysliph("Rakib", "Yes", 888)
print(rakib.status())

sakib = paysliph("Sakib", "no", 888)
print(sakib.status())
        