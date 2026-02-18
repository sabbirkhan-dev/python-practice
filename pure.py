# Pure Function 

"""
def pure_f(li):
    empty_li = []
    for item in li:
        empty_li.append(item*2)
    return empty_li
print(pure_f([1,2,3,4]))
"""


my_lis = [1,2,3]

def add_to_lis(lis, *items):
    nl = lis.copy()
    for item in items:
        nl.append(item)
    return nl

new_list = add_to_lis(my_lis, 4,5,6,7)

print(my_lis)
print(new_list)
