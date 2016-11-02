print "++++++++++Exercise 32: Loops and Lists++++++++++"

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
td_list = [[1,2,3],[4,5,6]]

# this first kind of for-loop goes through a list
for number in the_count:
  print "This is count %d" % number

# same as above
for fruit in fruits:
  print "A fruit of type: %s" %fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
  print "I got %r" % i

# we can also build list, first start with an empty one
# elements = []

# then use the range function to do 0 t0 5 counts
# for i in range(0, 5):
#   print "Adding %d to the list." % i
#   # append is a function that lists understand
#   elements.append(i)

# skipping loop
# elements = list(range(0, 5))
elements = range(0, 5)

# now we can print them out to:
for i in elements:
  print "Elements was: %d" %i

# 2d list interation
for i in td_list:
  for number in i:
    print 'Numbers in 2d list: %d' %number