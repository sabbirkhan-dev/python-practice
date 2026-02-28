"""# bill total function

def bill_total(bill):
    total = 0
    for k, v in bill.items():
        total += v
    return total

print(bill_total({"salad": 44, "tomato": 45}))
"""

# calculate tax bill

def tax_bill(percent, bill):
    tax = (percent / 100) * bill
    tax = round(tax, 2)
    bill_to = tax + bill
    return tax, bill_to

bill = float(input("Enter your bill: "))
total_tax = float(input("Enter your tax persentage: "))

tax, total_bill = tax_bill(total_tax, bill)

print(f"Your bill {total_bill}, your tax {tax}")
    