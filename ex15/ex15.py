print "++++++++++Exercise 15: Reading Files++++++++++"
from sys import argv

script, filename = argv

file = open(filename)

print "Here is your file content:"
print file.read()

print "-"*60

print "Enter file name again: "
second_filename = raw_input("> ")

print "Here is your second file content: "
print open(second_filename).read()
