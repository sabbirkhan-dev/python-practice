from abc import ABC, abstractmethod

class Smartphone(ABC):
    @abstractmethod
    def mobile(self):
        pass

class Samsung(Smartphone):
    def mobile(self): 
        print("Samsung Mobile is Best")

class Mi(Smartphone):
    def mobile(self):
        print("This is a Mi phone") 

s1 = Samsung()
s1.mobile() 

m1 = Mi()
m1.mobile() 

