print "++++++++++ Exercise 44: Inheritance Versus Composition ++++++++++"

class Other(object):

    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "child override()"

    def altered(self):
        print "Child, before parent altered()"
        self.other.altered()
        print "Child, after parent altered()"


child = Child()

child.implicit()

child.override()

child.altered()