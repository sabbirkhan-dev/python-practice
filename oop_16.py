class BankAccount:
    def __init__(self, name, blance, pin):
        self.name = name
        self.blance = blance
        self.__pin = pin

    def withdraw(self, amount, pin):
        if self.__check_pin(pin):      # calling private method
            self.blance -= amount
            print(f"Withdraw successful blance {self.blance}")
        else:
            print("Wrong password")

    def __check_pin(self,pin):     # Privet method
        if self.__pin == pin:
            return True
        else:
            return False
        
        
b1 = BankAccount("Tuhin", 50000, 4625)
b1.withdraw(3000, 4625) 


