class sum:
    def __init__(self, a):
        self.a = a 


    def __add__(self, other):
        return self.a + other.a
    
num1 = sum(22)
num2 = sum(22)
print(num1 + num2) 

str1 = sum("CSE")
str2 = sum(" 111")
print(str1 + str2) 



class data:
    def __init__(self, x):
        self.x = x

    def __gt__(self, word):
        if (self.x > word.x):
            return True
        else:
            return False
        
num3 = data(330)
num4 = data(66)

if num3 > num4:
    print("num3 in greter than num4")
else:
    print("num4 is greter than num3")


