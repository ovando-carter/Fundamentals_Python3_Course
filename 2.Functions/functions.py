
#
#
# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called "+title+" with " +str(row_count) + " rows.")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Applications", 10)


#
#
#calculating age and printing it
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")


#
#
#return multiple values
def get_boundaries(target, margin):
  low_limit = target - margin 
  high_limit = margin + target 
  return low_limit, high_limit

low_limit, high_limit = get_boundaries(100, 20)

low = low_limit
high = high_limit

print("Low limit value: " + str(low_limit))
print("High limit value: "+ str(high_limit))


#
#
#scope of function
current_year = 2048 #this time, current_year is not inside the function calculate_age. We have defined it before the function so it can be used within the function.

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)  
#print(age) #note the variable age only exsists within the function calculate_age. So this means that it can not be called outside of this function. 

print(calculate_age(1970))


#review task
def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats


message = repeat_stuff("Row ", 3)

lyrics = message + "Your Boat. "

song = repeat_stuff(lyrics)
#print(stuff)
#print(num_repeats)
print(repeat_stuff)
print(song)