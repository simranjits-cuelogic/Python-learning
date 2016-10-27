print "++++++++++Exercise 18: Names, Variables, Code, Functions++++++++++"

# this one is like your scripts with argv
def print_two(*args):
  for arg in args:
    print "argumnent: %r" % arg

# ok, that * args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" %(arg1, arg2)

# this just take one argument
def print_one(arg1):
  print "arg1: %r" %arg1

# this one takes no arguments
def print_none():
  print "I got nothing."

print_two('abc1', 'abc2', 'abc3', 'abc4')
print_two_again('xyz', 'abc')
print_one('opq')
print_none()