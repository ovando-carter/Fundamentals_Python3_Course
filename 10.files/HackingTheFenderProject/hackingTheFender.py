import csv # imports the csv module, alows us to read and write data for csv. 
import json # imports the json module

compromised_users = []

with open("passwords.csv") as password_file:#grabs each line seperatley and assigns keys from that line while creating a dictionary. 
  password_csv = csv.DictReader(password_file) 
  for password_row in password_csv:
    #print(password_row["Username"]) # names of all users who had their pasweords compramised. 
    compromised_users.append(password_row["Username"])

#print(compromised_users) # check to see if we get a list of compramised users. 

with open("compromised_users.txt", "w") as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

# Notifying the Boss Using JSON
# Your boss needs to know that you were successful in retrieving that compromised data. 

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict,boss_message) # will create a boss message in json format.

with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  """

  new_passwords_obj.write(slash_null_sig) # this will create a new password with the new slash_null_sig (signature)
