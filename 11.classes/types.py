## Types
print(type(5))
my_dict ={}
print(type(my_dict))
my_list = []
print(type(my_list))

##A class is a template for a data type. 
class Facade:
  pass # using pass to indicate that the body of the class was intentionally left blank so we don't cause an indentation error.

facade_1 = Facade() # Instantiating a class Facade

facade_1_type = type(facade_1)

print(facade_1_type)

## class variables
class Grade: 
  minimum_passing = 65 # here the class attribute is minimum_passing
  
## Methods are functions that are defined as part of a class.
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

## methods with arguments

class Circle: 
  pi = 3.14
  def area(self, radius): # this is how you define a method within a class.
    area = Circle.pi * radius ** 2
    return area

circle = Circle() # an instance of Circle saved to the variable circle.

pizza_area = circle.area(12/2) # remember, we have equated all the information in Circle into the variable circle. Then we are calling the variable area that exsists within Cricle using circle.area. Remeber, area(self,radius) takes in both self and radius, but here diameter/2 refers to the radius. Self requires no input. Here the diameter of the pizza = 12 inches

teaching_table_area = circle.area(36/2)

round_room_area = circle.area(11460/2)

## constructors
# ex 1
class Shouter:
  def __init__(self, phrase): # underscores before and after are used to initialise a newly created object. 
    # make sure phrase is a string
    if type(phrase) == str:

      print(phrase.upper())  # then shout it out

shout1 = Shouter("shout") # prints "SHOUT"

shout2 = Shouter("shout") # prints "SHOUT"

shout3 = Shouter("let it all out") # prints "LET IT ALL OUT"

# ex2
class Circle:
  pi = 3.14
  def __init__(self, diameter): #this is how we make a constructor
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

## Instance Variables
class Store:
  pass

alternative_rocks = Store() #defined a class object with Store
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks" # given them the instance atribute of .store_name
isabelles_ices.store_name = "Isabelle's Ices"

## attribute functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s")) # should pring 5 from sassafrass element and then 2 from ["a", "c", "s", "d", "s"] element.
    
## Self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

## everything is an object
print(dir(5))
print()

def this_function_is_an_object(string):
  return "This {} is the best in the world".format(string)

print(dir(this_function_is_an_object("plant")))

## string representation
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
