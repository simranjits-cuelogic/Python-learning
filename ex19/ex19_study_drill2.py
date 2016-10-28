print "++++++++++Exercise 19: Functions and Variables++++++++++"

def cheese_and_chrackers(cheese_count, boxes_of_chrackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_chrackers
  print "Man that's enought for party!"
  print "Get a blanket!\n"

# get input from user. bind this logic in method
def get_cheese_and_chrackers():
  default_value = 0
  cheese = int(raw_input("Amount of cheese? ") or default_value)
  charackers = int(raw_input("Amount of charackers? ")or default_value)
  return cheese, charackers


print "OR, we can use methods for getting input from user as well:"
amount_of_cheese, amount_of_chrackers = get_cheese_and_chrackers()

cheese_and_chrackers(amount_of_cheese, amount_of_chrackers)

print "and we can also combine the two, variables and math.(+2)"
cheese_and_chrackers(amount_of_cheese + 2, amount_of_chrackers + 2)
