## - sum values
def sum_values(my_dictionary):
  for value in my_dictionary:
    sum1 = sum(my_dictionary.values())
  return sum1

print(sum_values({"milk":5, "eggs":2, "flour": 3})) # should print 10
print(sum_values({10:1, 100:2, 1000:3})) # should print 6

## - Even Keys
def sum_even_keys(my_dictionary2):
  sum2 = 0
  for key in my_dictionary2.keys():
    if key%2 == 0:
      sum2 += my_dictionary2[key]
  return sum2

print(sum_even_keys({1:5, 2:2, 3:3})) # should print 2
print(sum_even_keys({10:1, 100:2, 1000:3})) # should print

## - Add Ten to dictonary
def add_ten(my_dictionary3):
  for value in my_dictionary3.keys(): 
    my_dictionary3[value] += 10
  return my_dictionary3

print(add_ten({1:5, 2:2, 3:3})) # should print {1:15, 2:12, 3:13}
#print(add_ten({10:1, 100:2, 1000:3})) # should print {10:11, 100:12, 1000:13}

## - Values That Are Keys
def values_that_are_keys(my_dictionary4):
  list_of_values = []
  for value in my_dictionary4.values(): # loop through all values in the dictionary.
    if value in my_dictionary4: # checks to see if the value is in my_dictionary
      list_of_values.append(value)
  return list_of_values

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10})) # should print [1, 4]
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100})) # should print ["a"]

## - largest value
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10})) # should print 1
print(max_key({"a":100, "b":10, "c":1000})) # should print "c"

#my attempt at finding the key for the largest value - does not work
#def max_key(my_dictionary5):
#  a = sorted(my_dictionary5.values())
#  b = a.pop()
#  print(a) # test to see if the values have been sorted in assending order.
#  print(b) # test to see if the highest number was taken off and added to b. 
#  for value in sorted(my_dictionary5.values()):
#    return my_dictionary5[-1].key()
  
#print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
#print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

## - word length dictionary - create 
def word_length_dictionary(words):
  word_lengths = {}
  for word in words: 
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
#print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

## - Frequency Count
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
    	freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1])) # should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0])) # should print {0:5}

## - unique variables
def unique_values(my_dictionary6):
  seen_values = []
  for value in my_dictionary6.values():
      if value not in seen_values:
        seen_values.append(value)
  return len(seen_values)

print(unique_values({0:3, 1:1, 4:1, 5:3})) # should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3})) # should print 1

## - Count First Letter
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters #should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]})) # should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]})) # should print {"S": 7}