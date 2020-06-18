This is my mehtod to solve the Larger Sum challenge. It works, but code academy will not accept it. 

def larger_sum(lst1, lst2):
  lst1_Tot = 0
  for i in lst1:
    lst1_Tot += i
  #return lst1_Tot
  #print(lst1_Tot) #this checks if the sum of the first list is 15 as expected. 
  lst2_Tot = 0
  for j in lst2:
    lst2_Tot += j
  #return lst2_Tot
  #print(lst2_Tot) # this checks if the sum of the second list is 12 as expected

  if lst1_Tot > lst2_Tot:
    return lst1
  elif lst1_Tot < lst2_Tot:
    return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))

## this is code academy solution - which is pretty much the same only more eligant
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))