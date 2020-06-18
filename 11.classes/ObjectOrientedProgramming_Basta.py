class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = [] # will return an array of all avaliable menus
    for menu in self.menus: #will loop through all menus
      if time >= menu.start_time and time <= menu.end_time: # the time falls within the start and end time, so is available. 
        available_menus.append(menu)
    return available_menus


class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self): #representation
    return self.name + ' menu avaliable from ' +str(self.start_time) + '-' + str(self.end_time) # this is how we do the string representations. It gives us the ability to show the name of the menue and the time that the manue is from and to when we call print().
  def calculate_bill(self, purchased_items): #method inside the class that will return the total price of the bill
    bill = 0 
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item] #note purchased_item is the key, for example 'pancakes'.
    return bill

#Brunch Menu
brunch_items = {
'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu("Brunch", brunch_items, 1100, 1600) # times given in 24 hr military time. 

Cost_items_bought = brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])

print("Brunch Total: " + str(Cost_items_bought))

#print(brunch_menu.name) #test, should print Brunch

#Early-bird Menu
early_bird = {
'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu("Early-bird", early_bird, 1500, 1800) # times given in 24 hr military time. 

Cost_early_bird_bought = early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

print("Early Bird Total: " + str(Cost_early_bird_bought))

#dinner Menu
dinner = {
'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu("dinner", dinner, 1700, 2300) # times given in 24 hr military time.


#kids Menu
kids = {
'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("kids", kids, 1100, 2100) # times given in 24 hr military time.

print(kids_menu)
print()

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store)

print(flagship_store.available_menus(2000)) #will print all menus available based on a time we put in. 


Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Arepa

arepas_items = {
'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepa = Business("Take a' Arepa", [arepas_place])

print(arepa.franchises[0].menus[0])