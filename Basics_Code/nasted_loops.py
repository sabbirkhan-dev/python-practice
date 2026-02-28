"""count = 0
for i in range(2):
    for l in range(2):
        print(l)
        count += 1
    print(i)
print(count)
"""

"""import time
start_time = time.time()

# outer loop
for i in range(5):
    # inner loop
    for h in range(20):
        print(0, end=" ")
    print()

print(round((time.time() - start_time), 2))

"""
# print(time.ctime())

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0
for index, num in enumerate(num_list):
    count += 1
    if num == 88:
        print(f'found your number {index}') 
        break
        
print(count)