from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, height, weight, colorEye):
        self.name = name
        self.height = height
        self.weight = weight
        self.colorEye = colorEye
    
    def __str__(self) -> str:
        return f"{self.name}; Height: {self.height}; Weight: {self.weight}; Color eye: {self.colorEye};"


    @abstractmethod
    def animalSay(self):
        return (f"{self.name} Roar: ")