## - lists
heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]



## - paird lists
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

ages = [['Aaron', 15], ['Dhruti', 16]]



## - listing newly paired lists
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names,dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

## - Empty lists - created so we can fill it up with some input entry at a later date. 
my_empty_list =[]


## - usign .append() to add items to a list
orders = ['daisies', 'periwinkle']

orders.append('tulips')

orders.append('roses')

print(orders)

## - Adding lists using +
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]

## - using range to create a list of numbers starting from 0 and ending at one less than the input number.
list1 = range(9) # this will have a list of 10 numbers [0,1,2,3,4,5,6,7,8,9]

list2 = range(8)

## - range 2
my_list = range(2, 9) 
print(list(my_list)) # this will print a list starting from 2, [2, 3, 4, 5, 6, 7, 8]

my_range2 = range(2, 9, 2)
print(list(my_range2)) # this will print a list starting from 2, and jumping in steps of 2, [2, 4, 6, 8]

my_range3 = range(1, 100, 10)
print(list(my_range3)) # this will print a list starting from 1 in steps of 10 but no greater than 100, [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

## - lists revied
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []

age.append(42)

all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, all_ages)

print(list(name_and_age))

ids = range(4)

print(list(ids))