print "++++++++++Exercise 33: While Loops++++++++++"

def show_numbers_using_while(number, increment_by = 1):
  i = 0
  numbers = []

  while i < number:
    print "At the top of i is %d" %i
    numbers.append(i)

    i+=increment_by
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    print "-"*50

  return numbers

def show_numbers_using_range(number):
  numbers = []

  for i in xrange(0,number):
    print "At the top of i is %d" %i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "-"*50

  return numbers

print "The numbers: "

# for num in show_numbers_using_while(10, 2):
#   print num
print show_numbers_using_while(10, 2)
print "*"*55

# for num in show_numbers_using_range(5):
#   print num
print show_numbers_using_range(6)
print "*"*55



