# Define animal class

class Animal():
    # Class is a cookie cutter for objects:
        # wraps it's characteristics and it behaviours
    # Define some characteristic (initialisation):
    def __init__(self, name, eyes, legs, age = 0):
        self.name = name
        self.bones = True
        self.alive = True
        self.number_eyes = eyes
        self.number_legs = legs
        self.age = age

    # Define some behaviours - these are known as Methods
        # Things an instance of an object can do
        # Functions that are dependent on an object type
    pass

    def eat(self, food):
        return 'NOM NOM NOM!' + food

    def mating(self):
        return '<3'

    def mate_calling(self):
        return 'Swipe right'

    def sleep(self):
        return 'Zzzzzz'

    def go_potty(self):
        return 'HHUMMMMM!!!'




