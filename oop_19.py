"""class A:
    temp = 4
    def __init__(self):
        self.y = self.temp -2
        self.sum = self.temp + 1
        A.temp = A.temp - 2
        self.methodA(3, 4)

    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + self.temp
        A.temp = A.temp + 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)

class B:
    x = 0
    def __init__(self, b = None):
        self.y, self.temp, self.sum = 5, -5, 2

        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
    def methodA(self, m, n):
        x = 2
        self.y = self.y + m + (self.temp)
        self.temp += 1
        x = x + 5 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
    
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)

    
        

a1 = A()
print(a1.temp)

b1 = B()
print(b1.temp)

b2 = B(b1)

"""



class A:
    temp = 4   # class variable (সব object share করবে)

    def __init__(self):
        self.y = self.temp - 2     # self.temp = 4 → y = 2
        self.sum = self.temp + 1   # sum = 5

        A.temp = A.temp - 2        # class variable change → temp = 2

        self.methodA(3, 4)         # constructor থেকে method call

    def methodA(self, m, n):
        x = 0                      # local variable

        self.y = self.y + m + self.temp
        # y = 2 + 3 + 2 = 7

        A.temp = A.temp + 1
        # class variable temp = 3

        x = x + 1 + n
        # x = 5

        self.sum = self.sum + x + self.y
        # sum = 5 + 5 + 7 = 17

        print(x, self.y, self.sum)
        # print: 5 7 17


class B:
    x = 0   # class variable

    def __init__(self, b=None):

        self.y, self.temp, self.sum = 5, -5, 2
        # initial values set

        if b == None:   # যদি object pass না করা হয়

            self.y = self.temp + 3
            # y = -5 + 3 = -2

            self.sum = 3 + self.temp + 2
            # sum = 0

            self.temp -= 2
            # temp = -7

        else:   # যদি object pass করা হয়

            self.sum = b.sum
            # অন্য object এর sum copy

            B.x = b.x
            # class variable copy

            b.methodB(2, 3)
            # অন্য object এর method call


    def methodA(self, m, n):

        x = 2

        self.y = self.y + m + self.temp
        # y change

        self.temp += 1
        # temp increase

        x = x + 5 + n
        # x change

        self.sum = self.sum + x + self.y
        # sum update

        print(x, self.y, self.sum)


    def methodB(self, m, n):

        y = 0

        y = y + self.y
        # local y = object y

        B.x = self.y + 2 + self.temp
        # class variable change

        self.methodA(self.x, y)
        # methodA call

        self.sum = self.x + y + self.sum
        # sum update

        print(self.x, y, self.sum)



# -------- object create --------

a1 = A()
# constructor run
# output: 5 7 17

print(a1.temp)
# output: 3


b1 = B()
# temp = -7

print(b1.temp)
# output: -7