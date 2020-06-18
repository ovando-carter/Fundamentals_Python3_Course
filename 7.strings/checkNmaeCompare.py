## - my version
sentence = "My name is Jamie"
name = "Jamie"
print(sentence.find(name.upper())) # this returns -1

def check_for_name(sentence, name):
  if sentence.find(name.upper()) or sentence.find(name.lower()) : # i cant figure this line out
    return True
  return False

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

## - their version
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie")) # should print True
print(check_for_name("My name is jamie", "Jamie")) # should print True
print(check_for_name("My name is Samantha", "Jamie")) # should print False