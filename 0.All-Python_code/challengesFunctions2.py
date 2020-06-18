#
#ex1 -
# Write your first_three_multiples function here
def first_three_multiples(num):
  a=num*1
  b=num*2
  c=num*3
  print(1)
  print(2)
  print(3)
  return c

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
#first_three_multiples(0)
# should print 0, 0, 0, and return 0


#
# ex 2- tip calculator
def tip(total, percentage):
  tip_amount = total*(percentage/100)
  return tip_amount


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0

#
#ex 3 - Bond, James Bond
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " +last_name
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
#print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

#
#ex 4 - dog years
def dog_years(name,age):
  dog_years = 7*age
  return name + ", you are " + str(dog_years) + " years old in dog years"  

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

#
#ex 5 - takes in four functions
# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a+b
  second = c-d
  third = first*second
  fourth = third%a
  print(first)
  print(second)
  print(third)
  return fourth

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0