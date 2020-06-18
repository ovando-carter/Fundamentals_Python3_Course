my_name = "Ovando"
first_initial = my_name[0] #this allows us to select the first letter of a word.


## - tem passwords
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6] #creates  a variable called temp_password by creating a slice out of the third through sixth letters of his last_name

## - creating a better account nema, since many people have the same last name
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name): 
  return first_name[:3] + last_name[:3]


new_account = account_generator(first_name, last_name)

print("A new account has been created with the name: " + str(account_generator(first_name, last_name)))

## - more and more passwords
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name): 
  return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  
print("A new account has been created with the name: " + str(password_generator(first_name, last_name)))

temp_password = password_generator(first_name, last_name)

## - negative index
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

print(company_motto[-2])
second_to_last = company_motto[-2]

print(company_motto[-4:])
final_word = company_motto[-4:] # this will print the last word of the string

## - fixing strings - note strings are immutable characters
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]

print("R" + first_name[-2:])

## - adding \ to change the functionality of inbuilt code elements
password = "theycallme\"crazy\"91" # this turns the " in to a normal " rather than defining a string.

## - creating len() from scratch = get_lenght()
def get_length(string):
  counter = 0
  for letter in string:
    #print(letter) #this is just here to test the loop
    counter += 1
  print(counter)
  return counter
    

get_length("Ovando")

## - checks if a letter exsists within a word.

def letter_check(word, letter): 
  for character in word:
    if character == letter:
      print(character)
      print(letter)
      return True
 return False
  

letter_check("strawberry", "a")

## - Strings and Conditionals (Part Two)
def contains(big_string, little_string):
  if little_string in big_string:
    print("True")
    return True
  else:
    print("False")
    return False
#contains("watermelon", "melon")
contains("watermelon", "berry")
    
def common_letters(string_one, string_two):
  commonLettersList = []
  for character in string_two:
    #print(character) #this should print all the individual chacraters in the 1st string
    letter = character    
    for character2 in string_one:
      #print(character2)
      if letter == character2:
        commonLettersList.append(letter)
  print(commonLettersList)
  return commonLettersList

## this is there way, much more elegant 
#def common_letters(string_one, string_two):
 # common = []
  #for letter in string_one:
   # if (letter in string_two) and not (letter in common):
    #  common.append(letter)
  #return common

common_letters("banana", "cream")

## - will print every letter with an even index
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")