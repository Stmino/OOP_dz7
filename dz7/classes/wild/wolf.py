from .wild import Wild


class Wolf(Wild):
   def __init__(self, name, height, weight, colorEye, place, date, leader):
      self.leader = leader
      super(Wolf, self).__init__(name, height, weight, colorEye, place, date)
   
   def animalSay(self):
        print(f"{super().animalSay()} уууУУУ")

   def __str__(self) -> str:
      if (self.leader == True):
        return f"{super().__str__()}; Area: {self.place}; Founding: {self.date}; The leader:"
      else: return f"{super().__str__()} Area: {self.place}; Founding: {self.date};"