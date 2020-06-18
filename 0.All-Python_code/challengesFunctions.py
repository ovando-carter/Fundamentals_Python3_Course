def some_function(some_input1, some_input2):
  # … do something with the inputs …
  return output
  
  def first_plus_last(lst):
  return lst[0] + lst[-1]
  
first_plus_last([1, 2, 3, 4]) #prints 5
first_plus_last([8, 2, 5, -8]) #prints 0
first_plus_last([-10, 2, 3, -4]) # prints -14


#
#ex2
def tenth_power(num):
  return num**10
#print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

#
#ex3 - square roots of numbers
def square_root(num):
  return num**(1/2)
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10

#
#ex4 - percentage
def win_percentage(wins, losses):
  return wins*100/ (wins + losses)
# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


#
#ex5 - average numbers 
def average(num1, num2):
  return (num1 + num2)/2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
#print(average(1, -1))
# The average of 1 and -1 is 0

#
#ex6 - get the remainder
# Write your remainder function here:
def remainder(num1, num2):
  return (2*num1)%(num2/2)

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

