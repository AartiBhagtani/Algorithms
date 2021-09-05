# parent class
class Car:
  class_variable = 2
  def __init__(self, name, modal_no):
    self.__name = name # private variable
    self._modal_no = modal_no # protected variable

  def car_details(self):
    return f"Name of car is {self.__name} and modal is {self._modal_no}"


car1 = Car('Audi', '8451')

print(car1._modal_no) # protected var accessible here
print(car1.car_details())
print(car1._Car__name) #name mangling for using private vars
print(car1.__name) # private var not accessible here

