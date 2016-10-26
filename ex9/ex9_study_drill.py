print "++++++++++Exercise 9: Printing, Printing, Printing++++++++++"

days = "Mon Tue Wed Thr Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are days: ", days
print "Here are the months: ", months
print "Here are the months:(s) %s"% months
print "Here are the months:(r) %r"% months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5  or 6.
  """


  def bla():
    # act as as decription
   """Print the answer"""
   print 42


bla.__doc__
 'Print the answer'

help(bla)
 Help on function bla in module __main__:

# print description
bla()
    Print the answer