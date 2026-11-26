import pickle


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


if __name__ == "__main__":
    car_1 = Car("audi", "a4", 2020)
    car_2 = Car("bmw", "x5", 2021)
    car_3 = Car("mercedes", "c-class", 2022)
    car_4 = Car("toyota", "camry", 2023)
    auto = [car_1, car_2, car_3, car_4]
    print(auto[2].get_descriptive_name())

    with open("auto.pkl", "wb") as file:
        pickle.dump(auto, file)
