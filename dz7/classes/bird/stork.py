
from .bird import Bird

class Stork(Bird):
    def __init__(self, name, height, weight, colorEye, fly):
        super().__init__(name, height, weight, colorEye, fly)
    
    def animalSay(self):
        print(f"{super().animalSay()} 'Tuck tuck' ")
    

    def __str__(self) -> str:
        return super().__str__()