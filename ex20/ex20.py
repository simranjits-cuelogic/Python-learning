print "++++++++++Exercise 20: Functions and Files++++++++++"

from sys import argv

scrpit, filename = argv

def print_all(f):
  print f.read()

def rewind(f):
  f.seek(0)

def print_a_line(f, line_number):
  print line_number, f.readline()

current_file = open(filename)

print "First let's print whole file: \n"
print_all(current_file)

print "Now let' rewind, kind of like a tape."
rewind(current_file)

print "Lets print three linkes:"

current_line = 1
print_a_line(current_file, current_line)

current_line = current_line + 1
print_a_line(current_file, current_line)

current_line = current_line + 1
print_a_line(current_file, current_line)

