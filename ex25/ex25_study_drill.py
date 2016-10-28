print "++++++++++Exercise 25: Even More Practice++++++++++"

def break_words(stuff):
  """This function will break up words for us"""
  return stuff.split(' ')

def sort_words(words):
  """Sorts the words"""
  return sorted(words)

def print_first_word(words):
  """Prints the first word after popping it off."""
  print words.pop(0)

def print_last_word(words):
  """Prints the last word after popping it off."""
  print words.pop(-1)

def sort_sentence(sentence):
  """Takes in a full sentence and returns the sorted words"""
  return sort_words(break_words(sentence))

def print_first_and_last(sentence):
  """Prints the first and last words of the sentence."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  """Sorted the words then prints the first and last one"""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)



def get_text1():
  text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
  Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"""
  return text

def get_text():
  return "Lorem Ipsum is simply dummy text of the printing and typesetting industry." \
  " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

breaked_words = break_words(get_text())

print "break_words"
print breaked_words
print "-"*30

print "sort_words"
print sort_words(breaked_words)
print "-"*30

print "print_first_word"
print_first_word(breaked_words)
print "-"*30

print "print_last_word"
print_last_word(breaked_words)
print "-"*30

print "sort_sentence"
print sort_sentence(get_text())
print "-"*30

print "print_first_and_last"
print_first_and_last(get_text())
print "-"*30

print "print_first_and_last_sorted"
print_first_and_last_sorted(get_text())
print "-"*30
