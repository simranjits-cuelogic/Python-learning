print "++++++++++Exercise 37: Symbol Review++++++++++"
# clear symbols -----(22 + 9)

# and         Logical and.  True and False == False
# continue    "Don't process more of the loop, do it again.  while True: continue"
# def         Define a function.  def X(): pass
# elif        Else if condition.  if: X; elif: Y; else: J
# else        Else condition.   if: X; elif: Y; else: J
# for         Loop over a collection of things.   for X in Y: pass
# from        Importing specific parts of a module.   from x import Y
# import      Import a module into this one to use.   import os
# in          Part of for-loops. Also a test of X in Y.   for X in Y: pass also 1 in [1] == True
# is          Like == to test equality.   1 is 1 == True
# while       While loop.   while X: pass
# from        Importing specific parts of a module.   from x import Y
# print       Print this string.  print 'this string'
# pass        This block is empty.  def empty(): pass
# lambda      Create a short anonymous function.  s = lambda y: y ** y; s(3)
# exec        Run a string as Python.   exec 'print "hello"'
# not         Logical not.  not True == False
# or          Logical or.   True or False == True
# return      Exit the function with a return value.  def X(): return Y
# try         Try this block, and if exception, go to except.   try: pass
# finally     Exceptions or not, finally do this no matter what.  finally: pass
# del         Delete from dictionary.   del X[Y]

# need to clear more on following symbols

# as          Part of the with-as statement.  with X as Y: pass
# assert      Assert (ensure) that something is true.   assert False, "Error!"
# break       Stop this loop right now.   while True: break
# class       Define a class.   class Person(object)
# except      If an exception happens, do this.   except ValueError, e: print e
# global      Declare that you want a global variable.  global X
# raise       Raise an exception when things go wrong.  raise ValueError("No")
# with        With an expression as a variable do.  with X as Y: pass
# yield       Pause here and return to caller.  def X(): yield Y; X().next()

# ____________Data Types (8)_____________

# Type______Description______Example_____

# True      True boolean value.                   True or False == True
# False     False boolean value.                  False and True == False
# None      Represents "nothing" or "no value".   x = None
# strings   Stores textual information.           x = "hello"
# numbers   Stores integers.                      i = 100
# floats    Stores decimals.                      i = 10.389
# lists     Stores a list of things.              j = [1,2,3,4]
# dicts     Stores a key=value mapping of things. e = {'x': 1, 'y': 2}

# Operator----(30)
# Operator__Description_______Example
# +         Addition          2 + 4 == 6
# -         Subtraction       2 - 4 == -2
# *         Multiplication    2 * 4 == 8
# **        Power of          2 ** 4 == 16
# /         Division          2 / 4.0 == 0.5
# //        Floor division    2 // 4.0 == 0.0
# %         String interpolate or modulus   2 % 4 == 2
# <         Less than             4 < 4 == False
# >         Greater than          4 > 4 == False
# <=        Less than equal       4 <= 4 == True
# >=        Greater than equal    4 >= 4 == True
# ==        Equal                 4 == 5 == False
# !=        Not equal             4 != 5 == True
# <>        Not equal             4 <> 5 == True
# ( )       Parenthesis           len('hi') == 2
# [ ]       List brackets         [1,3,4]
# { }       Dict curly braces     {'x': 5, 'y': 10}
# @         At (decorators)       @classmethod
# ,         Comma                 range(0, 10)
# :         Colon                 def X():
# .         Dot                   self.x = 10
# =         Assign equal          x = 10
# ;         semi-colon            print "hi"; print "there"
# +=        Add and assign        x = 1; x += 2
# -=        Subtract and assign   x = 1; x -= 2
# *=        Multiply and assign   x = 1; x *= 2
# /=        Divide and assign     x = 1; x /= 2
# //=       Floor divide and assign   x = 1; x //= 2
# %=        Modulus assign        x = 1; x %= 2
# **=       Power assign          x = 1; x **= 2