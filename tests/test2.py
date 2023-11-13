from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        raise NotImplementedError("Subclasses must implement the 'speak' method")
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Uncommenting the following line will result in an error, as Fish does not implement the required method.
class Fish(Animal):
    pass
