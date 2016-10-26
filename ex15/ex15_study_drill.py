print "++++++++++Exercise 15: Reading Files++++++++++"
from sys import argv

# unpacked arguments
script, filename = argv
# covering in try to catch invaid file name or format
try:
  file = open(filename, 'r') #open file in reading mode
  print "Here is your file content:"
  print file.read()
  file.close()
  print "-"*60

  print "Enter file name again: "
  second_filename = raw_input("-> ")

  print "Here is your second file content: "
  print open(second_filename, 'r').read() #open file in reading mode
# catch exception
except IOError:
  print "Wrong file name or format!"