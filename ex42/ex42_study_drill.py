print "++++++++++ Exercise 42: Is-A, Has-A, Objects, and Classes ++++++++++"

## Animal is-a object (yes, sort of confussion) look at the extra credit
class Animal(object):
    def legs(self):
        return 0

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def legs(self):
        return 4

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## sparrow is-a Animal
class Sparrow(Animal):
    def __init__(self, name):
        ## sparrow has-a name
        self.name = name

    def legs(self):
        return 2


animal = Dog('Tommy')
print animal.name
print animal.legs()

print '-'*15
sparrow = Sparrow('spar')
print sparrow.legs()
print sparrow.name

print '-'*15
animal = Animal()
print animal.legs()


# ## Person is-a object
# class Person(object):
#     def __init__(self, arg):
#         ## Person has-a name
#         self.name = name

#         ## Person has-a pet of some kind
#         self.pet = None

# ## Person is-a Person
# class Employee(Person):
#     def __init__(self, name, salary):
#         ## Employee is-a Person
#         ## initiating parent class
#         super(Employee, self).__init__(name)
#         ## Employee has-a salary
#         self.salary = salary

# ## Fish is-a object
# class Fish(object):
#     pass

# ## Salmon is-a object
# class Salmon(object):
#     pass

# ## Halibut is-a object
# class Halibut(object):
#     pass

# ## rover is-a Dog
# rover = Dog('Rover')

# ## satan is-a Cat
# satan = Cat('Satan')

# ## mary is-a Person
# mary = Person('Mary')

# ## marry has-a Cat
# mary.pet = satan

# ## frank is-a Employee is-a Person is-a object
# frank = Employee('Frank', 120000)

# ## frank has-a Dog
# frank.pet = rover

# ## flipper is-a Fish
# flipper = Fish()

# ## crouse is-a Salmon
# crouse = Salmon()

# ## harry is-a Halibut
# harry = Halibut()
