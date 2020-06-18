## - importing modules and using them. 
from datetime import datetime

current_time = datetime.now()
print(current_time)

## - random
import random

random_list = [random.randint(1,101) for i in range(101)]

randomer_number = random.choice(random_list)

print(randomer_number)

## - Namespaces and viewing data
import codecademylib3_seaborn

from matplotlib import pyplot as plt # here is have imported pyplot from a library called matplotlib and then aliasing it with the key word plt.

import random

numbers_a = range(1,13) # set equal to the range of numbers 1 through 12 (inclusive).

#numbers_b = [random.sample(12) for i in range(1000)]

numbers_b = random.sample(range(1000), 12) 

plt.plot(numbers_a, numbers_b)

plt.show() #You should see a graph of random numbers displayed. You’ve used two Python modules to accomplish this (random and matplotlib).

## - using decimal to mantain the number of decimal points
from decimal import Decimal

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.5300') * Decimal('0.6500')
print(four_decimal_points)

## - importing from a library
from libraryTest import always_three

always_three()