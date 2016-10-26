print "++++++++++Exercise 12: Prompting People++++++++++"

age = int(raw_input("How old are you? ") or 0)
height = int(raw_input("How tall are you? ") or 0)
weight = int(raw_input("How much do you weight? ") or 0)

print "So you're %r old, %s tall and %r heavy." %(age, height, weight)


"""
What does PYDOC do?
Pydoc is a documentation module for the programming language Python,
allows Python programmers to access Python's documentation help files,
generate HTML pages with documentation specifics,
and find the appropriate module for a particular job.
"""

# pydoc ---
# http://archive.oreilly.com/pub/post/programming_is_just_easier_wit.html
# Python interpreter by running pydoc as a script at the
# operating system's command prompt.
# For example, running
#    pydoc sys
# at a shell prompt will display documentation on the 'sys' module