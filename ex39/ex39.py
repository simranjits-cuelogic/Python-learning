print "++++++++++Exercise 39: Dictionaries, Oh Lovely Dictionaries++++++++++"

# create a mapping of states to abbreviation

states = {
  'Oregen' : 'OR',
  'Florida' : 'FL',
  'California' : 'CA',
  'New York' : 'NY',
  'Michigan' : 'MI'
}

# create ad basic set of states and some cities in then
cities = {
  'CA' : 'New York',
  'MI' : 'Detroit',
  'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

print '-' * 10
print "Michigan's has:", cities[states['Michigan']]
print "Florida's has:", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
  print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
  print "%s has the city %s" %(abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
  print "%s state is abbreviated %s and has city %s" %(
    state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by the state that might not be there
stage = states.get('Texas')

if not state:
  print 'Sorry, no Texas.'

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print 'The city for the state "TX" is: %s' % city