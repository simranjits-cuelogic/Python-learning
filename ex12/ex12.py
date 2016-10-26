print "++++++++++Exercise 12: Prompting People++++++++++"

age = int(raw_input("How old are you? ") or 0)
height = int(raw_input("How tall are you? ") or 0)
weight = int(raw_input("How much do you weight? ") or 0)

print "So you're %r old, %s tall and %r heavy." %(age, height, weight)