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

    # def __repr__(self):
    #     return self.show_creature
zoo = []


dna = {
    'size': ['huge', 'normal', 'small', 'tiny'],
    'nose': ['flat nose', 'long nose', 'wide nose', 'short nose'],
    'eyes': ['two eyes', 'three eyes', 'four eyes', 'five eyes'],
    'ears': ['large ears', 'long ears', 'small ears', 'earholes'],
    'covering': ['skin', 'fur', 'scales', 'feathers'],
    'bodylen': ['long body', 'medium body', 'short body', 'snakelike body'],
    'necklen': ['long neck', 'medium neck', 'short neck', 'neckless neck'],
    'forelegs': ['paws', 'hands', 'hooves', 'claws'],
    'hindlegs': ['paws', 'hands', 'hooves', 'claws'],
    'tail': ['no tail', 'short tail', 'medium tail', 'long tail'],
    'movement': ['slowly', 'normally', 'quickly', 'rapidly'],
    'qualities': ['agile', 'strong', 'alert', 'curious'],
    'dwelling': ['arboreal', 'aquatic', 'cavedwelling', 'domesticated']

}

#set instanc

##loads files
try:
    myfile = open('zoo.pickle', 'r')
    zoo = pickle.load(myfile)
    print 'loaded zoo'
except:
    print 'no content found'

def main():
    while True:
        #OPENING MENU
        #option 1
        #runs creator
        #option 2
        #opens management
        #option 3
        #quit
        print """Welcome to the creature creator.
        1 >--( creature creator )
        2 >--( view creatures )
        3 >--( remove creature )
        4 >--( quit )
        """
        user_input = int(raw_input("Please select an option: "))
        if user_input == 1:
            while True:
                #CREATOR
                #option 1
                #auto runs creator
                #when done, asks if you want to run again /pass
                #or end with breakanimal = Creature()
                print "Creature creation initiated."
                animal = Creature()
                creature_name = raw_input("What would you like to call your new creature? ")
                zoo[creature_name] = animal
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
                    print "Goodbye"
                    break
        elif user_input == 2:
            while True:
                #MANAGE
                #management menu
                #generates dynamic list
                #prints creature


                # creature_choice.show_creature
                # print lola.show_creature()

                name = raw_input("What creature would you like to examine?: ")
                for creature in zoo:
                    print creature
                    creature.show_creature()

                print "I'm broken"
                break
        elif user_input == 3:
            creature_name = raw_input("Creature to remove: ")
            del zoo[creature_name]
            print "Creature removed"
        elif user_input == 4:
            print "Goodbye"
            #saves files
            myfile = open('zoo.pickle', 'w')
            pickle.dump(zoo, myfile)
            myfile.close
            break
        else:
            print "Invalid input"

main()
