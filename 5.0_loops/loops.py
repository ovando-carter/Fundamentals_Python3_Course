## ex1 loops. 
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)
    
## ex2
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

print()
print("Board Games:")
for game in board_games:
  print(game)

print()
print("Sport Games:")
for sport in sport_games:
  print(sport)
  
## printing a message 5 times using loops
promise = "I will not chew gum in class"

for i in range(5):
  print(promise)
  
## infinite loops - are very unstable to the code. They will never stop. If this ever happens you must use control + c to terminate the loop. 
my_favorite_numbers = [4, 8, 15, 16, 42]

for number in my_favorite_numbers:
  my_favorite_numbers.append(1)# this code will continue to add 1 to the end of the list> There is no end.
  
## adding students from one list to another using loops, taking care not to create an infinite loop
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)
  
## using break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

print("Checking the breed list")
for breed in dog_breeds_available_for_adoption:
  print(breed)
  if breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
print("End of search!")

## using continue to skip over unwanted elements
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21: #if the persons age is below the drinking age of 21, then continue will cause the loop to skip over their entry. 
    continue
  print(age)
  
## using a while loop and .pop() to select students from the end of the all_students list and place them into a poetry class. The class has a limitation of only 6 spaces. 
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

index = 0 
while index < 6:
  A= all_students.pop()
  students_in_poetry.append(A)  
  index += 1
print(students_in_poetry)

## nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for data in location:
    scoops_sold += data #adds data in location to the scoops sold
print(scoops_sold) #prints the number of scoops sold


## - List Comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []

#for height in heights: # this will only take elements that are > 161 from the heights list. 
  #if height > 161:
    #can_ride_coaster.append(height) # this part will add the individuals heights to the list as it goes through the loops. 

can_ride_coaster = [height for height in heights if height > 161] #this is the short hand version

print(can_ride_coaster)

## converting temp in celcius to temp in farenheight
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp_in_c * (9/5) +32 for temp_in_c in celsius]

print(fahrenheit)

## final exercise in list comprehension
single_digits = list(range(10))

print(single_digits)

squares = []

for element in single_digits:
  print(element) #checks to see if the loop goes through each individual element. 
  squares.append(element ** 2)

print(squares)

cubes = [element ** 3 for element in single_digits] # this short hand is called list comprehension

print(cubes)