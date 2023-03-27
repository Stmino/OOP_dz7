import classes
import copy

class Zoo():

    all = []
    animal = classes.Wolf("Wolf", 1, 1, "White", "Belarus", "12.06.1888", True)
    all.append(copy.copy(animal))
    animal = classes.Cat("Cat", 1, 1, "Grenn", "Babe", "Cat", "Yes", "White", "10.10.1000", "Yes")
    all.append(copy.copy(animal))
    animal = classes.Dog("Dog", 1, 1, "Black", "Dog", "Dog", "No", "Dog", "No", "Yes")
    all.append(copy.copy(animal))
    animal = classes.Hen("Hen", 1, 1, "Green", 0)
    all.append(copy.copy(animal))
    animal = classes.Stork("Stork", 1, 1, "Green", 35)
    all.append(copy.copy(animal))