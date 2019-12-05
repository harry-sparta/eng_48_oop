from animal_class import *

class Reptile(Animal):

    def __init__(self, name, eyes, legs, number_heart_chambers, age = 0):
        super().__init__(name, eyes, legs, age)
        self.scales = True
        self.cold_blooded = True
        self.number_heart_chambers = number_heart_chambers


    def mate_calling(self): # this is our example of polymorphism example
        return 'Look at my scales! They look good.'

    def seek_heat(self):
        return 'Hmm. A bit chilly, lets get some sun.'

    def seek_shade(self):
        return 'Who turned on the heating in this world? Lets find some shade.'

    def prey(self):
        return 'Wait for it....wait.... and POUNCE!'

    def lay_eggs(self):
        return 'What you looking at? Never seen someone laying eggs before?'

    pass


