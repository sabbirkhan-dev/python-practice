# Strings in python are surrounded by either single quotation marks, or double quotation marks.

a = 'hello'      # single quotes
b = "hello"      # double quotes
print(a)         # hello
print(b)         # hello

multi_line = "this is a multi " \
    "line string example"
print(multi_line)  # this is a multi line string example


name = "John"   # 0123 = 4 (total 4 character)
print(name[0])   # J (index 0)
print(name[3])   # n (index 3)
print(len(name)) # 4 (total 4 character)



# Try these
city = "Dhaka"
print(city[0])       # D
print(city[-1])      # a (negative index ent to start)
print(len(city))     # 5

greeting = "Hello" + " " + "Sabbir!"
print(greeting)      # Hello Sabbir!

long_text = "Python is " \
            "awesome!"
print(long_text)




# Basic Data type and Function Cheatsheet

# Built-in Functions

print("I love Python")

name = input("Enter your name: ")
print("Hello " + name)

word = "Python"
print(len(word))

age = 25
text = str(age)
print("My age is " + text)

number = int("40")
print(number + 10)


def greet():
    print("Hello, welcome to Python")

greet()


def add(a, b):
    return a + b


result = add(5, 3)
print(result)




def total_price(price, quantity):
    return price * quantity


item_price = 50
qty = int(input("Enter quantity: "))


print("Total price:", total_price(item_price, qty))


# ✅ Quick Tips

# = → value assign

# == → compare

# : → block start

# Indentation → must

# def → function

# len() → length

# input() → user input