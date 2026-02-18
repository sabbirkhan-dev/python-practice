"""def div_of(a,b):
    return a / b

try:
    a = float(input("Enter your number: "))
    b = float(input("Enter your number: "))
    print(div_of(a,b))
    
except ZeroDivisionError as z:
    print("Zerodivision error", z)
except ValueError as e:
    print("Enter a number", e)
except Exception as u:
    print("Unexpected error", u)
    print(u. __class__)
    """
    
items = [1,2,3,4,5,6]
try:
    item = items[6]
    print(item)
except IndexError as i:
    print("Idex Error", i)
    
    
def divid_by(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, "Somthing went wrong!")
ans = divid_by(11,2)
print(ans)

# File open

try:
    with open("file dose not exit.txt", "r") as file:
        print(file.read())
except:
    print("Unable to local file")