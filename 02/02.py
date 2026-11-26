import json


data = [
    {"name": "Alice", "age": 30, "city": ("New York", "Los Angeles")},
    {"name": "Bob", "age": 25, "city": None},
    {"name": "Charlie", "age": 35, "city": "Chicago", "hobbies": ["reading", "traveling"]},
]

with open("data.sss", "w") as file:
    json.dump(data, file)


with open("data.sss", "r") as file:
    loaded_data = file.read()

print(loaded_data)
print("----------")
print(data[1])
print(data[1]["name"])
print("----------")
print(loaded_data[0:20])
print(type(loaded_data))

new_data = json.loads(loaded_data)
print(type(new_data))
print(new_data[1])
print(new_data[1]["name"])

print("----------")
with open("data.json", "r") as file:
    loaded_data_2 = json.load(file)

print(type(loaded_data_2))
print(loaded_data_2[1])
print(loaded_data_2[1]["name"])
