## - my method, including thinking and print() tests. 
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print()
print(highlighted_poems_list)

highlighted_poems_stripped = []
for i in range(len(highlighted_poems_list)):
  a = highlighted_poems_list[i].strip()
  highlighted_poems_stripped.append(a)
print()
print(highlighted_poems_stripped)

highlighted_poems_details = []
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(':'))

print()
print(highlighted_poems_details)

titles = []
poets = []
dates = []

#this is me thinking
#print(highlighted_poems_details[0])
#entry = highlighted_poems_details[0]
#print(entry[0])

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

print("Titles: " + str(titles))
print("Poets Names: " + str(poets))
print("Dates: " + str(dates))

print()
for i in range(0,len(highlighted_poems_details)):
    print()
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))




## - their method
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

    