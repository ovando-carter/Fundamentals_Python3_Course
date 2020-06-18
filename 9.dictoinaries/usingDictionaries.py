## - printing infor from dictionaries
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"]) # this allows you to access the zodiac sign for the key earth.

print(zodiac_elements["fire"])


## - errors
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

#print(zodiac_elements["energy"]) # before adding line 5 this will return  File "script.py", line 3, in <module> print(zodiac_elements["energy"]) KeyError: 'energy'

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"]) #make sure the print is after you had added the new info

## - try/except
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level["matcha"] = 30 # you can comment this out and see how the try/accept works. 

key_to_check = "matcha"
try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")
  
## - using get()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)

## - delete a key
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

print()
print(available_items)
print(health_points)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print()
print(available_items)
print(health_points)

## - dict_keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

## - Get All Values
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for values in num_exercises.values(): #loops through num_exercises
  total_exercises +=  values # addes values to the total_exercises
  print(total_exercises) # print to console
  
## - Get All Items
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + str(key) + "s.")
  
## - USING DICTIONARIES
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your "+key+" is the "+value+" card. ")

