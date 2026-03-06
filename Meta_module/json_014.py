import json

with open("Meta_module/data.json", "r") as file:
    data = json.load(file)
    
data["name"] = "Julhas Sikder"

with open("Meta_module/data.json", "w") as file:
    json.dump(data, file, indent = 4) 

print("Data is updated")

print(data) 

