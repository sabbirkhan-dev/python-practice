# m a d a m
# 0 1 2 3 4
"""
def is_palindrome(madam):
    start = 0
    end = len(madam) -1
    while start < end:
        if madam[start] !=madam[end]:
            return False
        start += 1
        end -= 1
    return True
        
print(is_palindrome("madadam"))   # True
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("racecar"))# True       
"""

# def check():
#     for x in [1, 2, 3]:
#         if x == 5:
#             return False
#     return True

"""
def is_Plaindrome(string_word):
    start_index = 0
    end_index = len(string_word) -1
    while start_index < end_index:
        if string_word[start_index] != string_word[end_index]:
            return False
        
        start_index += 1
        end_index -= 1
    return True

print(is_Plaindrome("aba"))
print(is_Plaindrome("abaa"))
"""
"""
def find_num(number):
    count = 0
    for x in range(100):
        if x == number:
            print("total", count)
            return x
        count += 1

print(find_num(9))"""


# def find_number_log(targe):
#     interations = 0
#     x = range(100)
#     left = 0
#     right = len(x) -1

#     while left <= right:
#         interations += 1
#         middle = (left + right) // 2
#         is_number = x [middle]

#         if targe == is_number:
#             print("interations", interations)
#             return middle
#         elif targe < is_number:
#             right = middle - 1
#         else:
#             left = middle + 1
        
#     return -1
    
# print(find_number_log(99))
        

"""
num = range(10)
left = 0
right = len(num) - 1

while left <= right:
    print(left, right)
    left += 1
    right -= 1
"""

"""
def find_number_log(targe):          # Binary search ফাংশন, targe = যে সংখ্যা খুঁজবো
    interations = 0                 # কয়বার লুপ ঘুরছে সেটা গোনার কাউন্টার
    x = range(100)                  # 0 থেকে 99 পর্যন্ত সংখ্যা
    left = 0                        # বাম দিকের শুরু index
    right = len(x) - 1              # ডান দিকের শেষ index (99)

    while left <= right:            # যতক্ষণ সার্চ করার জায়গা আছে
        interations += 1            # প্রতি লুপে iteration ১ করে বাড়ে
        middle = (left + right) // 2  # মাঝের index বের করা
        is_number = x[middle]       # মাঝের index-এর সংখ্যা 

        if targe == is_number:      # যদি target পাওয়া যায়
            print("interations", interations)  # কয়বার লুপ লেগেছে দেখাও
            return middle            # index রিটার্ন করো

        elif targe < is_number:     # target যদি মাঝের সংখ্যার চেয়ে ছোট হয়
            right = middle - 1      # ডান পাশ বাদ দাও

        else:                       # target যদি বড় হয়
            left = middle + 1       # বাম পাশ বাদ দাও
        
    return -1                       # পুরো লিস্টে না পেলে -1 রিটার্ন
    
print(find_number_log(-1))          # 99 খুঁজে ফাংশন কল 

"""

"""def inde_valu(arr,inx_val):
    for item in arr:
        if item == inx_val:
            return True
    return False

arr = [10, 20, 30, 40, 50]

result = inde_valu(arr, 30)
print(result)"""

def bubble_sort(arr):
    n = len(arr)              # total element সংখ্যা

    # OUTER LOOP (Pass control করে)
    # ডান পাশ (right side) ধীরে ধীরে sorted হয়ে যায়
    for i in range(n):

        # INNER LOOP (Left → Right compare করে)
        # j = left index
        # j+1 = right index
        for j in range(0, n - i - 1):

            # LEFT side element        RIGHT side element
            if arr[j] > arr[j + 1]:

                # swap (left বড় হলে right এ পাঠাও)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [60,10, 70, 20, 30,90, 40, 50,80]

print(bubble_sort(arr))   # function call
print(arr)         # sorted array print

print(arr[::-1]) 
arr = sorted(arr)
print(reversed(arr)) 