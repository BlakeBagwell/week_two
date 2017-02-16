"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0


    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evasion = 0


    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        crit_chance = random.randint(0, 4)
        if crit_chance == 4:
            print "CRITICAL!"
            enemy.receive_damage(self.power * 2)
            time.sleep(1.5)
        else:
            enemy.receive_damage(self.power)
            time.sleep(1.5)

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def recieve_bounty(self, enemy):
        if enemy.alive() == False:
            self.coins += enemy.bounty

    def receive_damage(self, points):
        hit_prob = 10 - self.evasion
        hit = random.randint(0, 10)
        if hit in range(0, hit_prob + 1):
            if points - self.armor > 0:
                self.health -= (points - self.armor)
                print "%s received %d damage." % (self.name, points)
            else:
                print "%s's armor is strong, negating all damage!" % (self.name)

            if self.health <= 0:
                print "%s is dead." % self.name
        else:
            print "%s dodges the attack!" % self.name



class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 4
        self.bounty = 3

    def receive_damage(self, points):
        self.health -= points
        heal = random.randint(0, 4)
        if heal == 3:
            self.health += 2
            print "%s received %d damage, but healed itself for 2 points!" % (self.name, points)
        else:
            print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name
        time.sleep(1.5)

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 1
        self.bounty = 3

    def receive_damage(self, points):
        get_hit = random.randint(0, 9)
        if get_hit == 9:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
            if self.health <= 0:
                print "%s is dead." % self.name
        else:
            print "The blade passes through %s's body... is this a dream?" % self.name
        time.sleep(1.5)

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 7
        self.power = 2

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s isn't dead. Something is very wrong..." % self.name
        time.sleep(1.5)

    def alive(self):
        return True

class Vampire(Character):
    def __init__(self):
        self.name = 'vampire'
        self.health = 6
        self.power = 2
        self.bounty = 5

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        self.health += self.power
        self.power += 1
        time.sleep(1.5)

class Fairy(Character):
    def __init__(self):
        self.name = 'fairy'
        self.health = 3
        self.power = 0
        self.bounty = 0
        self.magic = 3

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s heals %s" % (self.name, enemy.name)
        enemy.health += self.magic
        self.health -= 1
        time.sleep(1.5)

    def receive_damage(self, points):
        get_hit = randint(0, 3)
        if get_hit == 3:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
            if self.health <= 0:
                print "%s is dead." % self.name
        else:
            print "The %s avoids the strike!" % self.name
        time.sleep(1.5)



class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.recieve_bounty(enemy)
            print "You gained %r coins!" % enemy.bounty
            return True
            sleep(1.5)
        else:
            print "YOU LOSE!"
            return False



class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Supertonic(object):
    cost = 5
    name = 'super tonic'
    def apply(self, character):
        character.health += 10
        print "%s's health increased to %d." % (character.name, character.health)

class Armor(object):
    cost = 10
    name = 'armor'
    armor = 2
    def apply(self, hero):
        hero.armor += 2

class Cloak(object):
    cost = 10
    name = 'cloak'
    evasion = 2
    def apply(self, hero):
        if hero.evasion <= 6:
            hero.evasion += 2
        else:
            print 'The shop keeper snatches the cloak and refunds your money.'
            print 'This item cannot increase your evasion any further.'
            hero.coin += 10

class Stake(object):
    cost = 8
    name = 'wooden stake'






class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Supertonic, Armor, Cloak]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Medic(), Fairy(), Vampire(), Shadow()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
