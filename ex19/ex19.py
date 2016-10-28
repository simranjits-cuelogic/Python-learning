print "++++++++++Exercise 19: Functions and Variables++++++++++"

def cheese_and_chrackers(cheese_count, boxes_of_chrackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_chrackers
  print "Man that's enought for party!"
  print "Get a blanket!\n"

print "We can just give the function numbers directly:"
cheese_and_chrackers(20, 30)

print "OR, we can use varibales from our script:"
amount_of_cheese = 10
amount_of_chrackers = 50

cheese_and_chrackers(amount_of_cheese, amount_of_chrackers)

print "We can even do math inside too:"
cheese_and_chrackers(10 + 52, 5 + 4)

print "and we can also combine the two, variables and math."
cheese_and_chrackers(amount_of_cheese + 22, amount_of_chrackers + 201)

