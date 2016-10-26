print "Numarice Symbols"
print "+++++++++++++++++++++++++"

print "+ plus"
print "- minus"
print "/ slash"
print "* asterisk(multiplication)"
print "% percent(modulus)"
print "< less-than"
print "> greater-than"
print "<= less-than-equal"
print ">= greater-than-equal"

print "+++++++++++++++BODMAS++++++++++"

print "I will now count my chickens:"
# calculation to get total number of hens.
print "Hens:(30)", 25 + 30 / 6
# calculation to get total number of Roosters.
print "Roosters(25)", 100 - 25 * 3 % 4

# Some explations for correct and incorrent when calcuation deing done mannuly
print "Now I will count the eggs:(L <- R) Right -> (6 - 5 - 6) -> 6 - 5 + 6 = 7 "
print "Now I will count the eggs:(L -> R) Wrong -> (6 - 5 - 6) -> 1-6 = -5"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# calculation for conditional decision making
# < less-than
print "Is it true that (3 + 2 < 5 - 7)? => (5 < -2) => false"
print 3 + 2 < 5 - 7
# + plus
print "What is 3 + 2? => 5", 3 + 2
# - minus
print "What is 5 - 7? => -2", 5 - 7
print "Oh, that's why it's False."

# > greater-than
print "Is it greater? => true", 5 > -2
# greater-than-equal
print "Is it greater or equal? => true", 5 >= -2
# <= less-than-equal
print "Is it less or equal? => false", 5 <= -2