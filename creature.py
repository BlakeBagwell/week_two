import random
import time
import pickle

class Creature(object):
    def __init__(self):
        self.size = None
        self.nose = None
        self.eyes = None
        self.ears = None
        self.covering = None
        self.bodylen = None
        self.necklen = None
        self.forelegs = None
        self.hindlegs = None
        self.tail = None
        self.movement = None
        self.qualities = None
        self.dwelling = None

    def generate(self):
        #randomizes qualities and creates a new creature
        for trait_name, trait_options in dna.items():
            randomize = random.randint(0, 3)
            setattr(self, trait_name, trait_options[randomize])

    def show_creature(self):
        print """It is a %s creature with a %s, %s, and %s. It is covered in %s, has a %s and a %s.

        Its forelegs are %s, its hind legs have %s, and it has a %s.

        It moves %s and is a %s %s creature.""" % (self.size, self.nose, self.eyes, self.ears, self.covering, self.necklen, self.bodylen, self.forelegs, self.hindlegs, self.tail, self.movement, self.qualities, self.dwelling)

instructions = """
Gen Labs
=====================
1 >--( creature creator )
2 >--( manage creations )
    #will create a list of creatures and can
    select with a number
            once selected, you have a menu that will 1. list trait_options
            or 2. destroy the creature.
                if destroy, as for confirmation
3 >-- Quit
"""
# lists are 4 long so a loop can go through each list
#
# dictionary called dna
zoo = {}
dna = {
    'size': ['huge', 'normal', 'small', 'tiny'],
    'nose': ['flat nose', 'long nose', 'wide nose', 'short nose'],
    'eyes': ['two eyes', 'three eyes', 'four eyes', 'five eyes'],
    'ears': ['large ears', 'long ears', 'small ears', 'earholes'],
    'covering': ['skin', 'fur', 'scales', 'feathers'],
    'bodylen': ['long body', 'medium body', 'short body', 'snakelike body'],
    'necklen': ['long neck', 'medium neck', 'short neck', 'neckless neck'],
    'forelegs': ['paws', 'hands', 'hoves', 'claws'],
    'hindlegs': ['paws', 'hands', 'hoves', 'claws'],
    'tail': ['no tail', 'short tail', 'medium tail', 'long tail'],
    'movement': ['slowly', 'normally', 'quickly', 'rapidly'],
    'qualities': ['agile', 'strong', 'alert', 'curious'],
    'dwelling': ['arboreal', 'aquatic', 'cavedwelling', 'domesticated']

}
##loads files
try:
    myfile = open('zoo.pickle', 'r')
    zoo = pickle.load(myfile)
    print 'loaded zoo'
except:
    print 'no content found'
#### user inputs
#create a name (which creates a new object)
#have them generte the animal with if statement
#use method to tell the about their animal

def main():
    while True:


        animal = Creature()
        creature_name = raw_input("What would you like to call your new creature?")
        zoo[creature_name] = animal
        user_input = raw_input('Are you sure you want to play god? (y/n)')
        if user_input == 'y':
            animal.generate()
            print "Forming skeleton"
            time.sleep(1.0)
            print "Generating muscles"
            time.sleep(1.0)
            print "Waiting..."
            time.sleep(1.0)
            print "Waiting..."
            time.sleep(1.0)
            print "Waiting..."
            time.sleep(1.0)
            print "Creation complete!"
            time.sleep(1.0)

        if raw_input("Would you like to learn about your creature? (y/n)") == 'y':
            animal.show_creature()
        else:
            pass

        if raw_input("Would you like to keep creating? (y/n)") == 'y':
            pass
        else:
            print "God will punish you for your sins"
            #saves files
            myfile = open('zoo.pickle', 'w')
            pickle.dump(zoo, myfile)
            myfile.close
            break

main()


        #loops through keys in directory
