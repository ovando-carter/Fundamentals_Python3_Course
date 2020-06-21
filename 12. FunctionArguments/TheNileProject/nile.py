## The Nile
## The Nile fullfilment agency brings everything
## you could possibly want straight to your 
## door! Use your knowledge of Python functions
## and how to manipulate arguments to help 
## automate practices for the biggest 
## world-changing company.


from nile import get_distance, format_price, SHIPPING_PRICES # here is have imported information form the file nile.py.
from test import test_function # here is have imported information form the file test.py


## Shipping Costs Calculated Here:

# note, from_coords and to_coords are tuples that contain the latitude and then the longitude, see nile.py.
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'): # note shipping_type has been set to Overnight by defauly, becuase some customers forget to click this. It is key information so we need to put something in here.  
  #from_lat, from_long = from_coords # unpacking 
  #to_lat, to_long = to_coords # unpacking 
  distance = get_distance(*from_coords, *to_coords) #This is the same as doing this: distance = get_distance(from_lat, from_long, to_lat, to_long), just in a more compact way. Also, we don't need to unpack them in the previous two lines. 
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
    if cheapest_driver is None: # if the cheapest driver has not yet been set. 
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver    
  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)



# Define calculate_money_made() here


# Test the function by calling 
# test_function(calculate_money_made)
