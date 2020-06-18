inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
print("The number of items in Bob's Furniture warehouse is: " + str(inventory_len))

first = inventory[0] #this selects the first element in the variable inventory

last = inventory[-1] #this selects the last variable int the inventory

inventory_2_6 = inventory[2:6] #slects itens between 2 - 6.

first_3 = inventory[:3] #selects the first 3 elements of inventory

twin_beds = inventory.count('twin bed')
print()
print("The number of twin beds in the inventory are " + str(twin_beds))

inventory.sort()
print()
print("Inventory:")
print(inventory)