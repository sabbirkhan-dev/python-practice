set_1 = {1,2,3,4,5,6}
set_2 = {5,6,7,8,9,10}

print(set_1 | set_2)

print(set_1.union(set_2))

print(set_1.intersection(set_2)) # common value {5, 6}
print(set_1 & set_2) # common value {5, 6}


print(set_1 - set_2)

print(set_1.symmetric_difference(set_2))

# print(set_1[0])  Set unordered

if 5 in set_1:
    print("5 Available")