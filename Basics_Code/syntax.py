name = "Al-Amin"

if name == "Al-Amin":
    print(name)
    
x = 55
if x % 2 != 0:
    print("odd")

else:
    print("even")

if __name__=='__main__':
    n = int(input("input word: ").strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
        
    
