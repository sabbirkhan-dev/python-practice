
def sum_of(*args):
    sum_n = 0
    for x in args:
        sum_n += x
    return sum_n

print(sum_of(1,2,3))