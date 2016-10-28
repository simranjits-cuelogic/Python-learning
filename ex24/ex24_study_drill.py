print "++++++++++Exercise 22: What Do You Know So Far?++++++++++"

print "Let's practice everything."
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
whit logic so firmly planted
cannot discern \n the needs of love
not comprehend passions from intuition
and requiries an explanation
\n\t\twhere there is none.
"""
print "-"*30
print poem
print "-"*30

five = 10 -2 + 3 -6
print "This should be five: %s" % five

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starging point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates." %(beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# cause secret_formula returns more than on values so could be used as below
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point)

