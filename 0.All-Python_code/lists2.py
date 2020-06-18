## - finding the lenght of a range or list using len()
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

## - indexing
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]

print(len(employees))

print(employees[6])

## - printing thing last element
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))

last_element = shopping_list[-1] #this sellects the last element of the shopping list, even if we do not know how many elements the list has. 

element5 = shopping_list[5]

print()
print(last_element)
print()
print(element5)

## - slice lists
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']


beginning = suitcase[0:4]
print(len(beginning))
print(list(beginning))
print()
middle = suitcase[2:4] #this will only take the inner two elements of the list suitcase
print(list(middle))

## - slicing lists 2
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

start = suitcase[:3]# this will slect only the first 3 elements
end = suitcase[-2:] #this will select only the last two elements

## - counting votes
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

## - sorting lists 1
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)
print(cities)

## - using sorted()
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games) 
print(games)
print()
print(games_sorted) #this shows that sorted() does not change games, it just creates a new list that is sorted in alphabetical order. 