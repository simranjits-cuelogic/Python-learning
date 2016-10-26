print "++++++++++Exercise 14: Prompting and Passing++++++++++"
from sys import argv

script, name = argv

prompt = '> '

print "Hi %s!, I am %s script. I would like to ask you some questions." %(
  name, script)

print "Do you like %s?" % name
like = raw_input(prompt)

print "where do you live?"
location = raw_input(prompt)

print "What sort of computer do you have?"
computer = raw_input(prompt)


print """
Alright , so you said %r about liking me. you live in %s,
Not sure where that is. And you have a %s computer. Cool!!
""" %(like, location, computer)