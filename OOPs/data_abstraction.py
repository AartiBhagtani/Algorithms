from abc import ABC, abstractmethod

class Car:
  def __init__(self, name):
    self.name = name

  # abstract method
  def price():
    pass

  def name(self):
    return f"Name of car is {name}"

class Honda(Car):
  def price(self, price):
    return f"Price of car is {price} lakhs"

obj = Honda("amaze")  
print(obj.name)  
print(obj.price(12))

