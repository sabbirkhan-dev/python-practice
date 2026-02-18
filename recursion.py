
# Recursion

"""def re_fun(m):
    if m == 0:
        return
    
    print("Sabbir 1")
    re_fun(m-1,m)

re_fun(10)"""

# def find_factorial_loop(num):
#     if num < 0:
#         return 0
#     else:
#         factorial = 1
#         for i in range(1, num + 1):
#             factorial *= i
#         return factorial

# print(find_factorial_loop(4))



# Recursion Solution

"""def recursion_solution(number):
    if number == 1:
        return 1
    else:
        return number * recursion_solution(number -1)
    
print(recursion_solution(5)) """


"""
# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself.
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code: Initializing and calling the function
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')"""

"""
# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):   # hanoi নামের recursive function define করা হয়েছে

    # Base Condition
    if (disks == 1):                              # যদি মাত্র ১টা ডিস্ক থাকে
        print('Disk {} moves from tower {} to tower {}.'
              .format(disks, source, destination))  # সরাসরি source থেকে destination এ move দেখায়
        return                                    # function এখানেই শেষ

    # Recursive calls in which function calls itself.
    hanoi(disks - 1, source, destination, helper) # উপরের (disks-1) ডিস্ক source → helper এ পাঠানো

    print('Disk {} moves from tower {} to tower {}.'
          .format(disks, source, destination))   # সবচেয়ে বড় ডিস্ক source → destination এ পাঠানো

    hanoi(disks - 1, helper, source, destination) # helper থেকে (disks-1) ডিস্ক destination এ পাঠানো


# Driver code: Initializing and calling the function
disks = int(input('Number of disks to be displaced: '))  # ইউজারের কাছ থেকে মোট ডিস্ক সংখ্যা নেওয়া

'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')                      # function কল: A থেকে C তে ডিস্ক সরানো শুরু

"""

"""def hanoi(n, A, B, C):
    if n == 1:
        print(A, "->", C)
        return

    hanoi(n-1, A, C, B)
    print(A, "->", C)
    hanoi(n-1, B, C, A)

hanoi(3, 'A', 'B', 'C')"""

# print("sabbir")

word = "reversal"
print(word[::-1])

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("reversal"))


