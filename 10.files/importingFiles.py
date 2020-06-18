with open('welcome.txt') as text_file:# opens and saves the file welcome.txt to text_file variable. 
  text_data = text_file.read() #reads text file and saves data in file to a new variable
  print(text_data)
  
## reads specific lines in a txt file.
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
    
## read a specific line
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
  print(first_line)
  
## writing a file
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("No group comes to mind.")
#Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.
#It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.

## Appending to a File
# you can add a line of text to a file by using "a" for append. 
with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")


## you can still use the old syntax, but you have to remember to close the file. The new syntax means that you don't have to remember to close the file
#new syntax
with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
  print(setup)
  
#old syntax
close_this_file = open('fun_file.txt')
setup = close_this_file.readline()
punchline = close_this_file.readline()
print(setup)
close_this_file.close

## opening .csv files
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())
  
## reading a .csv file
import csv # this importats the cvs module.

list_of_email_addresses = []
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file) 
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
    
    
## selecting the key parts of a .csv file
import csv # this importats the cvs module.

each_rows_cool_fact = []
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file) 
  for row in cool_csv_dict:
    each_rows_cool_fact.append(row["Cool Fact"])
    print(each_rows_cool_fact)
    
## reading different types of .csv files
## A .csv file that has comms within the data as standard is not easy to separate based on the coma. But they might have something else. Data might be separated using ; instead. 

#import csv
#with open('addresses.csv', newline='') as addresses_csv:
#  address_reader = csv.DictReader(addresses_csv, delimiter=';')
#  for row in address_reader:
#    print(row['Address'])

#this example uses @ as a delimiter
import csv

with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for book in books_reader:
    isbn_list.append(book["ISBN"])
    print(isbn_list)
    
## writting a CSV File. 
# the following method will Iterate through the access_log list and add each element to the CSV using log_writer.writerow().
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)
    
## reading a JSON file
import json

with open('message.json') as message_json:
 pass
 message = json.load(message_json)

print(message['text']) # prints Now that's JSON! - if on code academy


## writing to a JSON file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
] # this is a dictionary

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json) #converts the data to JSON and then saves in to the file data.json