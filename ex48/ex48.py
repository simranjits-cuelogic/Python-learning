print "++++++++++ Exercise 48: Advanced User Input++++++++++"
"""breaking input"""
stuff = raw_input('> ')
words = stuff.split(' ')
print words


"""Turples"""
first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]
print sentence

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def check_number(input):
    if input.isdigit():
        return input
    else:
        return None


"""numaric input"""
print convert_number(raw_input('enter number > '))
print check_number(raw_input('enter number > '))

