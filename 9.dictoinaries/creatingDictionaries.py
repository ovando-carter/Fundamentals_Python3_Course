## introduction to dictionaries
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

num_cameras = {"backyard": 6 , "garage": 2, "driveway": 1}

print(sensors)


## - build your own dictionary
translations = {"mountain":"orod", "bread":"bass", "friend": "mellon", "horse": "roch"}


## - empty dictonary
my_empty_dictionary = {} # We can create an empty dictionary when we plan to fill it later based on some other input.


## - adding key pairs to the menu
animals_in_zoo = {} # empty menu

animals_in_zoo["zebras"] = 8 # adds new key pair to the menu

animals_in_zoo["monkeys"]=12

animals_in_zoo["dinosaurs"]=0

print(animals_in_zoo)


## - add multiple key pairs at once.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper":138475, "stringQueen": 85739}) # how to add multiple key pairs at once. 

print(user_ids)


## - over write
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"]="Viola Davis"

oscar_winners["Best Picture"]="Moonlight" # this will overwirte the info associated with the key Beast Picture.


## - List Comprehensions to Dictionaries
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}

## - final game
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]

playcounts = [78, 29, 44, 21, 89, 5]

plays = {songs:playcounts for songs, playcounts in zip(songs, playcounts) }

print(plays)

plays["Purple Haze"]=1

plays["Respect"] = 94 # the user has listened to this song 5 more times. SO here we are updating it.

library = {"The Best Songs":plays, "Sunday Feelings": {}} # creating a libray with two key pairs. The final one has an emplty list. 

print(library)
