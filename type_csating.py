# Implicit Conversion (Python do it)
a = 10        # int
b = 5.5       # float
result = a + b
print(result)      # 15.5 (auto int → float)
print(type(result)) # <class 'float'>

# Explicit Conversion
age_str = "25"          # form string 
age_int = int(age_str)  # convert to int
print(age_int + 5)      # 30 (calculation possible)

price = "99.99"
price_float = float(price)      # convert to float
print(price_float * 2)  # 199.98

num = 100
text = str(num)
print("Your number is " + text)  # concatenation possible


num_int = 55
print(num_int)

num_float = float(num_int)   # convert to float
print(num_float)

text_str = "55"
text_str_1 = "66"
print(text_str + text_str_1) # str

