
import classes
import zoo


def showAll():
    for i in range(len(zoo.Zoo.all)):
        print(f"{i+1}) {zoo.Zoo.all[i]}")


def showInfo(num):
    print(f"{num-1}) {zoo.Zoo.all[num-1]}")
    if (isinstance(zoo.Zoo.all[num-1], classes.Home)):
        zoo.Zoo.all[num-1].caressing()


def sayAll():
    for i in range(len(zoo.Zoo.all)):
        zoo.Zoo.all[i].animalSay()


