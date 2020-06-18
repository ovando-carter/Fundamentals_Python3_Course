## - my version
def username_generator(first_name,last_name):
  if (len(first_name) >= 3) and (len(last_name) >= 4):
    username = first_name[:3] + last_name[:4]
    return username
  else: 
    username = first_name + last_name
    return username

print(username_generator("Abe", "Simpson"))


def password_generator(first_name,last_name):
  password = last_name[3] + first_name[:3] + last_name[:3]
  return password
print(password_generator("Abe", "Simpson"))  

#this part does not work, but i am tired. 
def final_password(username):
  for i in range(0, len(username)):
    password += username[i-1]
  return F_password

## - code academy version - to me, this has not done what they asked me to do. So I am a little confused. 
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

print(username_generator("Abe","Simpson"))