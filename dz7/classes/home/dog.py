
from .home import Home


class Dog(Home):

    def __init__(self, name, height, weight, colorEye, name2, breed, vaccination, color, date, wool):
        self.wool = wool
        super(Dog, self).__init__(name, height, weight, colorEye, name2, breed, vaccination, color, date)
    
    def animalSay(self):
        print(f"{super().animalSay()} 'Gaf gaf'")
    
    def caressing(self):
        return (super().caressing())
    


    def __str__(self) -> str:
        return (f"{super().__str__()} {self.wool};")