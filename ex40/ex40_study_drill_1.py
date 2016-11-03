print "++++++++++ Exercise 40: Modules, Classes, and Objects ++++++++++"

class Color(object):
  """docstring for Color"""
  def __init__(self, color):
    self.first_color = color[0]
    self.second_color = color[1]

  def get_colors(self):
    print 'First color: ', self.first_color
    print 'Second color: ', self.second_color


class Vehicle(object):
  """docstring for Vehicle"""
  def __init__(self, name, model, color):
    self.name = name
    self.model = model
    self.color = Color(color)

  def get_vehicle_details(self):
    print '*' *10
    print "Vehicle name: ", self.name
    print "Vehicle model: ", self.model
    print "Vehicle colors: ", self.color.first_color, self.color.second_color
    print '*' *10

car = Vehicle("Car", 'Tata', ['Red', 'Black'])
truck = Vehicle("Truck", 'MC', ['Black', 'white'])
bus = Vehicle("Bus", 'Marocop', ['White', 'Grey'])

car.get_vehicle_details()
truck.get_vehicle_details()
bus.get_vehicle_details()





