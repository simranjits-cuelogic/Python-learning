# creating dynamic string and assign it to variable x
x = "There are %d types of people." %10

# assign varibale 'binary' and 'do_not' with value 'binary' and 'don't' respe.
binary = "binary"
do_not = "don't"

# creating dynamic string and inserting othrer strings for concatinate results
y = "Those who know %s and those who %s" %(binary, do_not) #string is put into other string

# printing x and y
print x
print y

# concat  varibale 'x' with given string.
print "I said: %r" % x #string is put into other string

# concat  varibale 'y' with given string.
print "I also said: '%s'" % y #string is put into other string

# assign boolem to variable named 'hilarious'
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# printing two seprate variables to combine results
print joke_evaluation % hilarious

# assign two variables with string value
w = "This is the left side of...."
e = "a string with a right side."

# printing two variables with plus sign(+) ie concatenate
print w + e
