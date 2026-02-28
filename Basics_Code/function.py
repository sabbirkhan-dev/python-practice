# def add(a,b):
#     return a + b

# print(add(44,2))

def cal_tax(bill, tax):
    tax_amount = bill * tax / 100
    total = bill + tax_amount
    return total

total_bill_with_Tax = cal_tax(100,15)
print(total_bill_with_Tax)


def cal_dis(bill, dis):
    dis_amount = bill * dis / 100
    total = bill - dis_amount
    return total, dis_amount

total_bill_with_Dis, disc = cal_dis(100,15)

print(total_bill_with_Dis, disc)