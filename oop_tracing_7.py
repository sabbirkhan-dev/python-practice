class Test3:
    def __init__(self):
        self.sum, self.y = 0, 0

    def methodA(self):
        x, y = 2, 3
        mgs = [0]
        mgs[0] = 3
        y = self.y + mgs[0]
        self.methodB(mgs[0], mgs)
        x = self.y + mgs[0]
        self.sum = x + y + mgs[0]
        print("2:", x, y, self.sum) 

    def methodB(self, mg1, mg2):
        x = 0
        self.y = self.y + mg2[0]
        x = x + 33 + mg1
        self.sum = self.sum + x + self.y
        mg2[0] = self.sum + mg1 
        mg1 = mg1 + x + 2
        print("3:", "x", x , "Self.y", self.y, "Self.sum", self.sum) 

t3 = Test3() 
t3.methodA()
t3.methodA()
t3.methodA()



