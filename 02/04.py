import csv


data_loaded = []
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    keys = next(reader)
    for row in reader:
        item = {}
        for i in range(len(keys)):
            item[keys[i]] = row[i]
        data_loaded.append(item)

print(data_loaded)
print(data_loaded[1])
print(data_loaded[1]["name"])
