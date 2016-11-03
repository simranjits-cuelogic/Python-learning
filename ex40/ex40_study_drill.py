print "++++++++++ Exercise 40: Modules, Classes, and Objects ++++++++++"

class Vehicle(object):
  """docstring for Vehicle"""
  def __init__(self, name, model, color):
    self.name = name
    self.model = model
    self.color = color

  def get_vehicle_details(self):
    print '*' *10
    print "Vehicle name: ", self.name
    print "Vehicle model: ", self.model
    print "Vehicle color: ", self.color
    print '*' *10

car = Vehicle("Car", 'Tata', 'Red')
truck = Vehicle("Truck", 'MC', 'Black')
bus = Vehicle("Bus", 'Marocop', 'White')

car.get_vehicle_details()
truck.get_vehicle_details()
bus.get_vehicle_details()





