menu = ["espresso", "cappuccino", "latte", "cortado", "mocha", "coffee"]
def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
    
# map_coffee = map(find_coffee, menu)
# print(map_coffee)

# for x in map_coffee:
#     print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for y in filter_coffee:
    print(y)

data = (range(0,11,2))
for x in data:
    print(x)