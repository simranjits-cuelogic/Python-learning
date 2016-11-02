print "++++++++++Exercise 33: While Loops++++++++++"

i =0
numbers = []

while i < 10:
  print "At the top of i is %d" %i
  numbers.append(i)

  i+=1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i
  print "-"*50

print "The numbers: "

for num in numbers:
  print num