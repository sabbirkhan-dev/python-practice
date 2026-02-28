name = input("What is your name? :")
print(f"Welcome {name}")

nam = int(input("Enter your first number: "))
nam_2 = int(input("Enter your last number: "))

print(f"Your addition number is {nam + nam_2}")


n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
    

