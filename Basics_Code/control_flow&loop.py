# names = ["Rahim", "Karim", "Sabbir", "Rina"]
"""num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

cont = 0
for index, num in enumerate(num_list):
    cont += 1
    if num == 88:
        print("Number Found", index)
        break
    if num > 45:
        print("Over 45")
        
    else:
        print("Under 45")
        
print("total loop count", cont)
"""
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0

for num in num_list:
    if num > 40:
        print("over 40", num)
    else:
        print("Under 40")
        
    count += 1
        
print(f"count total len {count}")