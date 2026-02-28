data = [2,3,5,7,11,13,17,19,23,29,31]
# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list", data)

# Ex2: List comprehension: creating a different list with updated values

new_data = [x*2 for x in data]
print(new_data)

# Ex3: With an if-condition: Multiples of four:

fourx = [x for x in data if x % 4 == 0]
print(fourx)

# Ex4: Alternatively, we can update the list with the if condition as well

fourxsub = [x-1 for x in data if x % 4 == 0]
print(fourxsub)
# Ex5: Using range function:

nines = [x for x in range(100) if x % 9 == 0]
print(nines)

# List comprehension:

data = [2,3,5,7,11,13,17,19,23,29,31]
# data_ = [x + 3 for x in data]
# print(data_) 

# Regular for loop:

for x in range(len(data)):
    data[x] = data[x] + 3
    print(x, data[x]) 

# {key: value for item in sequence} 


# Using range() function and no input list

using_range = {x:x*2 for x in range(11)}
print(using_range)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

num_dict = {keys:value for keys,value in zip(number, months)}
print(num_dict) 

for k,v in zip(number,months):
    print(k,v)

for index, (k,v) in enumerate(zip(number,months)):
    print(k,v)

# def square(num):
#     return num * 2

# print(square(33))

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")

def infinity_counter():
    n = 2
    while True:
        yield n
        n += 2  


count = infinity_counter()
print(next(count))
print(count)


new_data = [2,3,5,7,11,13,17,20,23,28,31]
gen_object = (x for x in new_data if x % 2 == 0)  # only output even number
print(gen_object)
print(type(gen_object))

for item in gen_object:
    print(item, end=".....")

a = [[96], [69]]

print(''.join(list(map(str, a))))