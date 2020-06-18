## - Every Three Numbers
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91)) # will print [91, 94, 97, 100]

## - Remove Middle
def remove_middle(lst, start, end):
  new = lst[:start] + lst[end+1:] # this will select all elements up to the start, and select all entries after the end point
  return list(new)
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3)) # will print [4, 23, 42]

## - More Frequent Item
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  elif lst.count(item1) == lst.count(item2):
    return item1
  
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

## - Double Index
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([3, 8, -10, 12], 2))

## - Middle Number
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))

