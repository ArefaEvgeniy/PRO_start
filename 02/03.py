import csv


data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]

with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(data)

rows_name = []
rows = []
for row in data:
    item = []
    if not rows_name:
        for key in row.keys():
            rows_name.append(key)
    for value in row.values():
        item.append(value)
    rows.append(item)

print(rows_name)
print(rows)

with open("data_2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(rows_name)
    writer.writerows(rows)
