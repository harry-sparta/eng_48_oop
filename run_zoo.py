from animal_class import *
from reptile_class import *

# Create 2 reptiles
reptile_1 = Reptile('Ringo', 2, 4, 17)
reptile_2 = Reptile('Susan', 2, 4, 16)

# Make the reptiles sleep
print(reptile_1.sleep())
print(reptile_2.sleep())
print(reptile_1.mate_calling())
print(reptile_1)