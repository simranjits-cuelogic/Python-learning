print "++++++++++Exercise 4: Variables And Names++++++++++"

# assigning cars
cars = 100

# assigning space_in_a_car
space_in_a_car = 4

# assigning drivers
drivers = 30

# assigning passerngers
passerngers = 90

# assigning cars_not_driven
cars_not_driven = cars - drivers

# assigning cars_driven
cars_driven = drivers

# calculationg and assigning carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# calculationg and assigning average_passengers_per_car
average_passengers_per_car = passerngers / cars_driven

# Printing all calculated details
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We car transport", carpool_capacity, "people today."
print "We have", passerngers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
