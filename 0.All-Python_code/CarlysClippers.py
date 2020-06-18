hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price

print("The total of all prices: " + str("{:.2f}".format(total_price)))

average_price = total_price/len(prices)

print()
print("Average Haircut Price: " + str("{:.2f}".format(average_price)))

new_prices = [price - 5 for price in prices]
print()
print("The new prices are the old price minus 5: " + str(new_prices))

total_revenue = 0

i = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]

print()
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue/7

print()
print("Average Daily Revenue: " + str(average_daily_revenue))

hair_cuts_under_30 = []
print()
i = 0
#for i in range(len(new_prices)):
   #if new_prices[i] < 30:
    #print(hairstyles[i])
    #hair_cuts_under_30.append(hairstyles[i])
       
cuts_under_30 = [hair_cuts_under_30.append(hairstyles[i]) for i in range(len(new_prices)) if new_prices[i] < 30] # in list comprehension form

print("List of hiar cuts under 30: " + str(hair_cuts_under_30))

## - Exponents
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers: 
      new_list.append(base ** power)
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))