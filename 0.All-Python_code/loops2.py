## - divisible by 10
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))



## - Greetings
def add_greetings(names):
  empty_list = []
  for name in names:
    empty_list.append("Hello, " + name)
  return empty_list

print(add_greetings(["Owen", "Max", "Sophie"]))



## delete starting even numbers
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

##- odd indicies
def odd_indices(lst):
  new_list = []
  for index in range(1, len(lst), 2):
    new_list.append(lst[index])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

## larger sum
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for i in lst1:
    sum1 += i
  for i in lst2:
    sum2 += i
  if sum1 >= sum2:
    return lst1
  else:
    return lst2
    
print(larger_sum([1, 9, 5], [2, 3, 7]))

## Over 9000
def over_nine_thousand(lst):
  sum1 = 0
  for i in lst: 
    sum1 += i
    if sum1 >= 9000:
      break
  return sum1
  print(sum1)
  
print(over_nine_thousand([8000, 900, 120, 5000]))

## the max num
def max_num(nums):
  for number in nums: 
    sorted_list = sorted(nums)
    #print(sorted_list) #this is a test to see if it sorted the numbers from smallest to highest
    maxNum = sorted_list.pop() # this will take off the last element, the highest number, and add it to a new list
  #print(maxNum) #this tests if maxNum holds the highest number
  return maxNum

print(max_num([50, -10, 0, 75, 20]))

## Same Values
def same_values(lst1, lst2): 
  new_lst = []
  for i in range(len(lst1)): 
    if lst1[i] == lst2[i]:
      new_lst.append(i)
  return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))