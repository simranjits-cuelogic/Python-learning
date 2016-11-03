print "++++++++++ Exercise 44: Inheritance Versus Composition ++++++++++"

class Parent(object):

    def override(self):
        print "Parrent override()"

    def implicit(self):
        print "Parrent implicit()"

    def altered(self):
        print "Parrent altered()"

class Child(Parent):
    def override(self):
        print "child override()"

    def altered(self):
        print "Child, before parent altered()"
        super(Child, self).altered()
        print "Child, after parent altered()"

parent = Parent()
child = Child()

parent.implicit()
child.implicit()

parent.override()
child.override()

parent.altered()
child.altered()