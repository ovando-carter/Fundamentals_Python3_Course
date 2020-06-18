## - finding the last name of the authors
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

# from here to the print(), I am just working out how to use each par seperatley. 
a = ""
a += author_names[0]
print(a)

new_a = a.split()
print(new_a)

new_a_pop = new_a.pop()
print(new_a_pop)
print()

empty_list = [] #remember, I do not want the new list in the loop. It will make many new lists, but I only want one. 
for i in range(len(author_names)):
  a = ""
  a += author_names[i]
  new_a = a.split()
  new_a_pop = new_a.pop()
  empty_list.append(new_a_pop)
print(empty_list) #this is to check if the new empty_list has what it should have in it. 

author_last_names = empty_list # i could simplify this further, but I like to see how I worked out this solution. 