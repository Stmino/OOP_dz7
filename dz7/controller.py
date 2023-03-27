import model
import view
import zoo



def ButtonClick():
    num = view.menu()
    match num:   
        case 1:
            model.showAll()
            ButtonClick()
        case 2:
            model.sayAll()
            ButtonClick()
        case 3:
            exit()



def sayAnimal():
    model.showAll()
    num = view.sayAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        ButtonClick()
    else:
        model.sayAnimal(num)
        ButtonClick()


def infoAnimal():
    model.showAll()
    num = view.showAnimalMenu()
    if (num > len(zoo.Zoo.all)):
        ButtonClick()
    else:
        model.showInfo(num)
        ButtonClick()
