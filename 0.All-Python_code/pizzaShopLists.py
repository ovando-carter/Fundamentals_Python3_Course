toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)

print(toppings)
#print(num_pizzas)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")


pizzas = list(zip(prices, toppings))
pizzas.sort()
print()
print(pizzas)

cheapest_pizza = pizzas[0]
#print(cheapest_pizza)
priciest_pizza = pizzas[-1]
#print(priciest_pizza)
three_cheapest = pizzas[:3]
print()
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print()
print(num_two_dollar_slices)