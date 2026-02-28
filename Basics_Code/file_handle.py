"""try:
    with open("test.txt", mode="r", encoding = "utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File name not found")
except Exception as e:
    print(f"An error occurred {e}")
    """
# with open("test.txt", mode="r", encoding="utf-8") as file:
#     content = file.readline()
#     print(content)

"""
try:    
    with open("new_file.txt", 'w') as file:
        file.writelines(["This is a first line 1\n",
                         "This is a second line 2 \n",
                         "This is third line 3"])
except FileNotFoundError as e:
    print("Error", e)"""
    
    
"""with open("new_file.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1, line2)"""
    
"""
# read (n)

with open("new_file.txt", mode="r") as file:
#    content = file.read()
    print(file.read(4))  # print only the 4 characters
    
"""

"""try:
    with open("test.txt", "r") as f:
        for file in f:
            print(file.strip())
except FileNotFoundError as e:
    print("Not Found", e)"""
    
    
"""with open("test.txt", "r") as file:
    print(file.readline(31))"""
    
"""    
with open("test.txt","r") as file:
    line = file.readlines()
    print(len(line))
    
    for files in line:
        print(files.strip())
      """  
        
import random
names = []
try:
    file_name = input("Enter your File name: ")
    
    for line in file_name:
        line_1 = line.strip()
        if line_1:
            names.append(line_1)
    with open(file_name, "r") as file:
        names = file.read().splitlines()
        print(random.choice(names))
        
except FileNotFoundError as e:
    print(e, "File not found")
except Exception as e:
    print(e, "error")