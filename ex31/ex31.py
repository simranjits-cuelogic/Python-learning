print "++++++++++Exercise 31: Making Decisions++++++++++"

print "Your enter a dark room with two doors. \
Do you go through door #1 or door #2?"

door = raw_input("> ")
if door == '1':
  print "There's a giant bear here eating a cheese cake. What do you do?"
  print "1. Take a cake."
  print "1. Screem at the bear."

  bear = raw_input("> ")

  if bear == '1':
    print "The bear eats your face off . Good Job!"
  elif bear == '2':
    print "The bear eats you legs off. Good Job!"
  else:
    print "Well, doing %s is probably better. Bear runs away." % bear

elif door == '2':
  print "You stare into the endless abyss at Cthulhus's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothescpins."
  print "3. Understanding revolvers yelling melodies."

  insanity = raw_input("> ")

  if insanity == '1' or insanity == '2':
    print "Your body survives powered by a mind of jello. Good job!"
  else:
    print "The insanity rots your eyes into a pool of muck. Good job!"

else:
  print "your stumble around and fall on a knige and die. Good job!"



