# parent class
class Car:
  def __init__(self, name, modal_no):
    self.name = name
    self.modal_no = modal_no

  def car_details(self):
    return f"Name of car is {self.name} and modal is {self.modal_no}"

# child class
class Honda(Car):
  def __init__(self, modal_no, name):
    self.name = name
    self.modal_no = modal_no

  def car_details(self):
    return f"Name of Honda car is {self.name} and modal is {self.modal_no}"

car1 = Car('Honda', '8452')
car2 = Honda('8451', 'Amaze')

print(car1.car_details())
print(car2.car_details())

