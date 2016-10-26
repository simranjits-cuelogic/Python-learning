print "++++++++++Exercise 5: More Variables and Printing++++++++++"

name = 'Simar'
age = 25 #not a lie
height = 71 #inches
cms_per_inch = 2.54 #2.54 aprox cms in one inch

weight = 180 #lbs
pound_per_kg = 2.2 #2.2 aprox pound in one kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall approx. %f cms." %(height, height*cms_per_inch)
print "He's %d pound heavy approx. %f kg." %(weight, weight/pound_per_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(
  eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." %(
  age, height, weight, age + height + weight)

print "More format characters"
print "d -- Signed integer decimal: %d" %2.2
print "i -- Signed integer decimal: %d" %2.3
# The alternate form causes a leading zero ("0") to be inserted between
# left-hand padding and the formatting of the number if the leading character
# of the result is not already a zero.
print "o -- Unsigned octal. %o" %23

print "u -- Unsigned decimal. %u" %23

# The alternate form causes a leading '0x' or '0X'
# (depending on whether the "x" or "X" format was used) to be inserted
# between left-hand padding and the formatting of the number
# if the leading character of the result is not already a zero.
print "x -- Unsigned hexadecimal (lowercase). %x" %23
print "X -- Unsigned hexadecimal (uppercase). %X" %23
print "e -- Floating point exponential format (lowercase). %e" %23
print "E -- Floating point exponential format (uppercase). %E" %23
print "f -- Floating point decimal format. %f" %23
print "F -- Floating point decimal format. %F" %23
print 'g -- Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise. %g' % 23
print 'G -- Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise. %G' % 23
print 'c -- Single character (accepts integer or single character string). %c' %'S'

# The %r conversion was added in Python 2.0
print 'r -- String (converts any python object using repr()). %r' % 23

# If the object or format provided is a unicode string,
# the resulting string will also be unicode
print 's -- String (converts any python object using str()). %s' % 23

# print '% -- No argument is converted, results in a "%" character in the result. %' %