print "++++++++++Exercise 16: Reading and Writing Files++++++++++"

from sys import argv

# unpacked arguments
script, filename = argv

print "We are gonna clear %r file" %filename
print "If you don't want to do this, press Ctrl+c",
print "else hit return to continue.."

raw_input("? ")

# openning file
print "Opening file: %s" %filename
# 'w' is file opening mode ie write mode
# 'r' is for read mode
# 'a' is for append mode
file = open(filename, 'w')

# you don't need file to be truncate if you are opennig file as 'w' write mode
# writing something in file will overide the existing data.
print "Turncate file..."
file.truncate()


# write text into file
print "Writing file:"
new_line = '\n'
line1 = raw_input("What is your name? ")
line2 = raw_input("Where do you stay? ")

file.write(line1 + new_line + line2)
file.close()

# Displaying file content
print "File content:"
print open(filename).read()