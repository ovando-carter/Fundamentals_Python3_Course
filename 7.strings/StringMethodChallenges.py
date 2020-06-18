## - Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("mississippi")) # should print 4
print(unique_english_letters("Apple")) # should print 4

## - count X - counts the number of times a character is found in a word. 
def count_char_x(word, x):
  return word.count(x)

print(count_char_x("mississippi", "s")) # should print 4
#print(count_char_x("mississippi", "m")) # should print 1

## - it can also work for a group of chacracters
def count_multi_char_x(word, x):
  return word.count(x)

print(count_multi_char_x("mississippi", "iss")) # should print 2
#print(count_multi_char_x("apple", "pp")) # should print 1

## - substring between
def substring_between_letters(word, start, end):
  s = word.find(start)
  e = word.find(end)
  if s > -1 and e > -1:
  	return(word[s+1:e])
  return word

print(substring_between_letters("apple", "p", "e")) # should print "pl"
#print(substring_between_letters("apple", "p", "c")) # should print "apple"

## - X length
#sentence = "i like apples"
#word_list = []
#word_list = sentence.split(" ")
#print(word_list) 
#

word_list = []  
def x_length_words(sentence, x):
  word_list = sentence.split(" ")
  for word in word_list:
    if len(word) < x:
      return False
  return True
    
print(x_length_words("i like apples", 2)) # should print False
#print(x_length_words("he likes apples", 2)) # should print True

## - check name
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie")) # should print True
print(check_for_name("My name is jamie", "Jamie")) # should print True
print(check_for_name("My name is Samantha", "Jamie")) # should print False

## - Every Other Letter
#word = "Codecademy"
#letters = word[0:-1:2]
#print(letters) #testing code outside of the function.

def every_other_letter(word): 
  letters = word[0:-1:2]
  return letters
  print(letters) # if works, should print Cdcdm (for the first one)

print(every_other_letter("Codecademy")) # should print Cdcdm
#print(every_other_letter("Hello world!")) # should print Hlowrd
#print(every_other_letter("")) # should print

## - Reverse
def reverse_string(word):
  return word[::-1] # reverses and prints the word
  
print(reverse_string("Codecademy")) # should print ymedacedoC
#print(reverse_string("Hello world!")) # should print !dlrow olleH
#print(reverse_string("")) # should print

## - Make Spoonerism
def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:]
  new_word2 = word1[0] + word2[1:]
  single_string = new_word1 + " " + new_word2
  return single_string
  print(single_string)

print(make_spoonerism("Codecademy", "Learn")) # should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!")) # should print wello Horld!
#print(make_spoonerism("a", "b")) # should print b a

## - Add Exclamation
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy")) # should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn")) # should print Codecademy is the best place to learn
