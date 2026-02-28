tuple_1 = (1,2,3,4,22,33,44,1,2,3,4)
print(tuple_1.count(1))

print(tuple_1.index(44))

# tuple_1[4]= 5 #TypeError: 'tuple' object does not support item assignment

for tup in tuple_1:
    print(tup)