print "++++++++++Exercise 21: Functions Can Return Something++++++++++"

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def what_puzzle():
  # what = add(10, subtract(15, multiply(20, divide(25, 2))))
  # what = add(10, subtract(15, multiply(20, 12)))
  # what = add(10, subtract(15, 240))
  # what = add(10, -225)
  # what = -215
  return add(age, subtract(height, multiply(weight, divide(iq, 2)))) #-215

print "Let's do some math wih just functions!"

age = add(5, 5) #10
height = subtract(18, 3) #15
weight = multiply(5, 4) #20
iq = divide(100,4) #25

print "Age: %d Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)
print "Here is a puzzle."
print "That becomes: ", what_puzzle(), "Can you do it by hand?"
