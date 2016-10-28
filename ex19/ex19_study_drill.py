print "++++++++++Exercise 19: Functions and Variables++++++++++"

def cheese_and_chrackers(cheese_count, boxes_of_chrackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_chrackers
  print "Man that's enought for party!"
  print "Get a blanket!\n"

print "OR, we can use varibales from our script:"
default_value = 0
amount_of_cheese = int(raw_input("Amount of cheese? ") or default_value)
amount_of_chrackers = int(raw_input("Amount of charackers? ") or default_value)

cheese_and_chrackers(amount_of_cheese, amount_of_chrackers)

print "and we can also combine the two, variables and math.(+2)"
cheese_and_chrackers(amount_of_cheese + 2, amount_of_chrackers + 2)
