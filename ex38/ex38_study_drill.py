print "++++++++++Exercise 38: Doing Things to Lists++++++++++"

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Songs", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

for x in xrange(1,10):
  # check for break
  if len(stuff) == 10:
    break
  next_one = more_stuff.pop()
  print "Adding: ", next_one
  stuff.append(next_one)
  print "There are %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some things with stuff."

# 1st indexed value from list
print stuff[1]
# last element... same as ruby
print stuff[-1]
# get the last element from the list
print stuff.pop()
# join content of list as string with space seprator
print " ".join(stuff)
# get 3to5 indexed value from list. equal to range(3,5)
print "#".join(stuff[3:5])
