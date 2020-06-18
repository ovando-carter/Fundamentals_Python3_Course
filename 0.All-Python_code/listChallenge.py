## - using Append Sum
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])#this will add 1 + 2 = 3, and then add it to lst
  lst.append(lst[-1] + lst[-2])# this will add 2 + 3 = 5, and then add it to lst
  lst.append(lst[-1] + lst[-2]) #this will add 3 + 5 = 8, and then add it to the lst
  return lst

print(append_sum([1, 1, 2]))

## - Larger List (The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.)
def larger_list(lst1,lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  elif len(lst1) == len(lst2):
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

## - More than N (will return true when the item is greater than n, and False in any mother case)
def more_than_n(lst, item, n):
  if lst.count(item) > n: 
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

## - Append Size - appends a list by adding the number of that list to the list. 
def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))

## - combine sort
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

