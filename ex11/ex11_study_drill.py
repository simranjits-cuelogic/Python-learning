print "++++++++++Exercise 11: Asking Questions++++++++++"

print "How old you are?",
age = int(raw_input() or 0) #adding 'or 0' for handling blank input

print "How tall you are?",
height = int(raw_input() or 0)

print "How much do you weight?",
weight = int(raw_input() or 0)

# %r is for debugging purpose thats why output like '5\'11"'
# Replace it with %s for showing proper format of string
print "So, you're %r old, %s tall and %r heavy." %(
  age, height, weight)

print "Output: ", age, height, weight


