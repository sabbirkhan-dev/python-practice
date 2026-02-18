list1 = [1,2,3,4,5,6]
print(*list1) # 1 2 3 4 5 6
print(list1)  # [1, 2, 3, 4, 5, 6]

print(list1, sep=" ")

list1.pop(0)  # del index number 1

del list1[1]

print(list1)


for num in list1:
    print(f"Value...{num}")
    
sabbir = 2,"d", True
print(type(sabbir))


# Great! Let's start with **Python lists**. Take a look at this code:

# ```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list[0] = 10
print(my_list)

# What do you expect the output of this code to be, and why?


employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

def emp_id (id):
    for emp in employee_list:
        if emp[0] == id:
            return{"id": emp[0], 'name': emp[1], 'department': emp[2]} 
    return "Id emp not found"
        

print("id",emp_id(12458))    


   
