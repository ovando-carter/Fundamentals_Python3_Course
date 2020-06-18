#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

## my version makes more sense to me. But will have to look in to this more
def reversed_list(lst1, lst2):
  lst2.reverse()
  print(lst2) #test to see if lst2 has been reversed.
  for i in lst1: 
    if lst1[i] == Lst2[i]:
      return True
    else:
      return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))