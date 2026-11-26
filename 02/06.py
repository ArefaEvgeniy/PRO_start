import pickle


with open("auto.pkl", "rb") as file:
    auto_loaded = pickle.load(file)

print(auto_loaded)
print(auto_loaded[2].get_descriptive_name())
