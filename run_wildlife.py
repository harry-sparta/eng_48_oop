from animal_class import *
from reptile_class import *

# How to create an object
# Creating an instance of Animal class
simba = Animal('simba', 3, 1)

# Checking data type
# print(simba)
# print(type(simba))

# Calling methods on an object
# print(simba.eat('chicken'))
# print(simba.go_potty())
# print(simba.sleep())

# Call the attributes of an object
# print(simba.age)
# print(simba.bones)
# print(simba.number_legs)

# Creating an instance of Reptile class
ringo = Reptile('Ringo', 3, 1, 8)

# Calling methods on an object of Reptile class
print(ringo.eat('food'))
print(ringo.seek_heat())

# Animal class doesn't have seek)heat
# print(simba.seek_heat())

# Redefining Reptile Class mate_calling methods from Animal default
print(simba.mate_calling())
print(ringo.mate_calling())