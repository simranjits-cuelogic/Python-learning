print "++++++++++Exercise 16: Reading and Writing Files++++++++++"

from sys import argv

# unpacked arguments
script, filename = argv

# write text into file
print "Writing file:"
new_line = '\n'
line1 = raw_input("What is your name? ")
line2 = raw_input("Where do you stay? ")

# openning file
print "Opening file: %s" %filename

with open(filename, "r+") as f:
  data = f.read()
  print data
  # Cursor to required position. Index 0 means starting of file,
  # 1 for current positon and 2 for end of the file.
  # Now operaton starts at seeked postion
  f.seek(2)
  f.write(line1 + line2)
  # f.truncate()