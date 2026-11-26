from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        ...

    def __str__(self):
        return f"{self.__class__.__name__} named {self.name}"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


cat_1 = Cat("Whiskers")
dog_1 = Dog("Buddy")
# obj_1 = Animal("Generic Animal")

print(cat_1.speak())
print(dog_1.speak())
# print(obj_1.speak())
