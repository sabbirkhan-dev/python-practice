
def total_bill(**kwargs):
    bill_total = 0
    for key, value in kwargs.items():   #key not use
        bill_total += value
    return round(bill_total)
    
print(total_bill(coffee = 3, tea = 5, juice = 30, apple = 12))

a = [[96], [69]]

print(''.join(list(map(str, a))))
        