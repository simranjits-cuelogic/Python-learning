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
file = open(filename, 'w')

# going to clear file
print "Turncate file..."
file.truncate()

print "Writing file:"
# write text into file
new_line = '\n'
line = raw_input("What is your name? ")
file.write(line)
file.write(new_line)

line = raw_input("Where do you stay? ")
file.write(line)
file.write(new_line)

print "Finally! closing file."
file.close()
