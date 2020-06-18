gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"): # this line checks if the argument passed to the gamer parameter has both name and avaliability as keys.
        gamers_list.append(gamer) # this line adds gamer to gamers list if the above is true.
    else: 
        print("Gamer list is missing critical information")
        
kimberly = {
    "name":"Kimberly Warner", 
    "availability":["Monday", "Tuesday", "Friday"]
}

add_gamer(kimberly,gamers)

print()
print(gamers)
print()

# adding a few more gamers to the list
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


#To calculate which nights would have the most participation, we need to create a frequency table which correlates each day of the week with gamer availability.
def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }

count_availability = build_daily_frequency_table()

print()
print("count_availability Dictionary: " + str(count_availability) + "\n")

# For each day in the gamer's availability, add one to that date on the frequency table.
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list: 
        for day in gamer['availability']:
            available_frequency[day] += 1


            
# find the best night to run Abruptly Goblins!
calculate_availability(gamers, count_availability)
print(count_availability)

#finding the best day for game night
def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night

game_night = find_best_night(count_availability)
print()
print(game_night)

##
def available_on_night(gamers_list, day):
    people_avaliable = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            people_avaliable.append(gamer)
    return people_avaliable

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)

## this is the way they wrote it. Much more sucinct
#def available_on_night(gamers_list, day):
#    return [gamer for gamer in gamers_list if day in gamer['availability']]
#attending_game_night = available_on_night(gamers, game_night)
#print(attending_game_night)
##

#  generating and email for the participants
form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

#sending emailß
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))
        
send_email(attending_game_night, game_night,"Abruptly Goblins!")

# list of people who can not attend
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

# emailing the ones that can't make it
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")

