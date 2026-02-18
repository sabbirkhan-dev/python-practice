bill_total = float(input("Enter your total bill: "))

discount = bill_total * 0.10  # 10/100
discount_02 = bill_total * 0.20  # 20/100

if bill_total >=100 and bill_total <=200:
    print("You got a discount becouse your bill is grater then 100")
    bill_total = bill_total - discount
    
elif bill_total >= 200:
    print("You got a 20% Discount")
    bill_total = bill_total - discount_02
    
else:
    print("Sorry your bill is less then 100")
    
print(f"Your total bill is {bill_total}")


loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))
