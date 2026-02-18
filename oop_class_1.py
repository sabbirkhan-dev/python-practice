class Myclass:
    a = 4

    def hello(self):
        print("Hello World!")

c1 = Myclass()
c1.hello()


class my_claculator:
    def product(self, *num):
        count = 1
        for x in num:
            count *= x
        print(count)

c1 = my_claculator()
c1.product(22, 2) 

