# parent class
class Car:
  class_variable = 2
  def __init__(self, name, modal_no):
    self.name = name
    self.modal_no = modal_no

  def car_details(self):
    return f"Name of car is {self.name} and modal is {self.modal_no}"

# child class
class Audi(Car):
  def __init__(self, modal_no, name):
    self.name = name
    self.modal_no = modal_no

car1 = Audi('8451', 'Audi')

print(car1.modal_no)
print(car1.car_details())

