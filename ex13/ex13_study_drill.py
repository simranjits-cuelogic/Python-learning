print "++++++++++Exercise 13: Parameters, Unpacking, Variables++++++++++"

from sys import argv

script, name, age = argv
color = raw_input("Ohh! Forgot to have your eye color, please enter: ")

print "-"*60
print "Cool!, you are %s, %d years old with %s shade eyes!" %(
  name, int(age), color)
print "_"*60