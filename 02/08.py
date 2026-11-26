class Auto(object):
    cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self._model = model
        self.__year = year
        self.incriment_cars()

    @classmethod
    def incriment_cars(cls):
        cls.cars += 1

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.make == other.make
        return False

    def __add__(self, other):
        if isinstance(other, Auto):
            return (
                Auto(f"{self.make} & {other.make}",
                     f"{self._model} & {other._model}",
                     max(self.__year, other.__year))
            )
        return NotImplemented

    def display_info(self):
        print(f"{self.__year} {self.make} {self._model}")

    @staticmethod
    def calculate(h, a):
        return (h**2 + a**2)**0.5

    def get_year(self):
        if self.__year < 2000:
            return self.__year + 10
        return self.__year


car = Auto("Toyota", "Camry", 2023)
print(car.make)  # Accessible
print(car._model)  # Accessible but not recommended
# print(car.__year)  # Not accessible, will raise AttributeError
print(car._Auto__year)  # Accessible through name mangling
car.display_info()  # Displays the car information
print(car.get_year())  # Accesses the private year attribute through a method

car_2 = Auto("Honda", "Civic", 1995)
print(car == car_2)
car_3 = car + car_2
car_3.display_info()

print(car.calculate(3, 4))

print(Auto.calculate(3, 4))

print(f"Total cars created: {Auto.cars}")


class Truck(Auto):
    cars = 0

    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload Capacity: {self.payload_capacity} kg")


truck_1 = Truck("Ford", "F-150", 2022, 1000)
truck_2 = Truck("Chevrolet", "Silverado", 2021, 1200)
print(Truck.cars)
print(Auto.cars)
