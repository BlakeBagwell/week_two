import random

class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, person):
        person.health -= self.power

    def nothing(self):
        pass

    def life_check(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print "The %s has %d health and %d power." % (self, self.health, self.power)

    def __repr__(self):
        return self.name


hero = Character('Hero', 10, 5)
goblin = Character('Goblin', 6, 2)

def game():
    print """
    In this simple RPG game, the hero fights the goblin. He has the options to:

    1. fight goblin
    2. do nothing - in which case the goblin will attack anyway
    3. flee

    """
    while hero.life_check() and goblin.life_check():
    #run the game
        hero.print_status()
        goblin.print_status()
        input = raw_input("(1) (2) (3) ")

        if input == "1":
            hero.attack(goblin)
            goblin.attack(hero)
        elif input == "2":
            print "The goblin makes a quick stab while you aren't paying attention."
            goblin.attack(hero)
        elif input == "3":
            break
        else:
            print "Invalid input %r" % input

    if hero.life_check() and goblin.life_check():
        print "You flee like a coward!"
    elif hero.life_check():
        print "You have slayed the goblin!"
    elif goblin.life_check():
        print "You have died!"
    elif hero.life_check() == goblin. life_check():
        print "You both die."


game()
#now outside of loop
#we check who is dead and tell the user if they
#won or lost

#now that the game is built
#we call the function of the game
