print "++++++++++ Exercise 49: Tuples++++++++++"


year_born = ("Paris Hilton", 1981)

print year_born


a = 10
b = 20

print "a: ", a
print "b: ", b

(a, b) = (b, a)

print "a: ", a
print "b: ", b

tub = (a, b)  # tuple packing
(aa, bb) = tub  # tuple unpacking

print "aa: ", aa
print "bb: ", bb
