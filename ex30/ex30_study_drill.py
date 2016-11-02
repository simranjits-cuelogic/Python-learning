print "++++++++++Exercise 30: Else and If++++++++++"

people = 20
cars = 20
trucks = 25

if cars > people:
  print "We should take the cars."
elif cars > people:
  print "We should not take the cars."
else:
  print "We can't decide."

if trucks > cars:
  print "That's too many trucks."
elif trucks < cars:
  print "Maybe we could take the truks."
else:
  print "We still can't decide."

if people > trucks:
  print "Alright, let's just take the trucks."
else:
  print "Fine, let's stay home then."

# only first true block will be executed
if False:
  print "First block"
elif True:
  print "Second block"
elif True:
  print "Third block"
else:
  print "fourth block"


if not(trucks > cars) or trucks < cars:
  print "1st block"
else:
  print "2nd block"

# Invalid syntax,
# if not:
#   print "1st block"
# else:
#   print "2nd block"

# O is treated as False, non 0 (-ve)is True
if 0:
  print "codition with 0 -- True block"
else:
  print "codition with 0 -- False block"

if 1:
  print "codition with non-0 -- True block"
else:
  print "codition with non-0 -- False block"

if not(not(True) and 1 == 1 and 0 != 1):
  print "complex condition -- True block"
else:
  print "complex condition -- False block"

if not(1 == 1 and 0 != 1):
  print "complex condition -- True block"
else:
  print "complex condition -- False block"

