print "++++++++++Exercise 17: More Files++++++++++"
from sys import argv
from os.path import exists

scritp, from_file, to_file = argv
new_line = '\n'
target_file = open(to_file, 'a')
target_file.write(new_line + open(from_file).read())
target_file.close()

print "Alright, all done."

# out_file.close()
# Need of file.close()
# close method of a file object flushes any unwritten info and close the file
# object, after it not reading/writing can be done.