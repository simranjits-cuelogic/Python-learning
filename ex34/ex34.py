print "++++++++++Exercise 34: Accessing Elements of Lists++++++++++"

def ordinal(n):
  if 10 <= n % 100 < 20:
      return str(n) + 'th'
  else:
     return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

for index, animal in enumerate(animals):
  ordinal_number = ordinal(index+1)
  # NOTE: need to work on ordinal_word
  # ordinal_word = ordinal(index)
  # print "The %s (%r) animal is at %r and is a %s."
   # %(ordinal_word, ordinal_number, index, animal)
  print "The %r animal is at %r and is a %s." %(ordinal_number, index, animal)
  print "The animal at %s is the %s animal and is a %s." %(index, ordinal_number, animal)
  print "-"*50
