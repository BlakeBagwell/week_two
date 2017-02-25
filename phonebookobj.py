phonebook object

class would be people

setting entries would create a person
and add it to to the object that is the phonebook

look up is a function
that prints details of a person object

delete removes a person object

list prints all person objects

add auto save and auto Load

Quit

class Phonebook(object):
    phonebook = {}

    def user_nav():
        ### calls the other methods based on input

    def look_up(self, name):
        print #person and info
    def set_entry(self):
        name = raw_input("Name: ")
        phonebook[name] = {
        'number': raw_input("Number: "),
        'email': raw_input("Email: "),
        'website': raw_input("Website: ")
        }


    def delete_entry():
        name = raw_input("Name: ")
        del phonebook[name]
        print "ENTRY DELETED"

    def list_all():
        #print phonebook


while True:

    print instructions

    user_input = int(raw_input("What do you want to do (1-7)? "))

    if user_input == 1:
        name = raw_input("Name: ")
        print phonebook[name]

    elif user_input == 2:
        name = raw_input("Name: ")
        phonebook[name] = {
        'number': raw_input("Number: "),
        'email': raw_input("Email: "),
        'website': raw_input("Website: ")
        }

    elif user_input == 3:
        name = raw_input("Name: ")
        del phonebook[name]
        print "ENTRY DELETED"

    elif user_input == 4:
        print phonebook

    elif user_input == 5:
        print "SAVING ENTRIES..."
        myfile = open('phonebook.pickle', 'w')
        pickle.dump(phonebook, myfile)
        myfile.close

    elif user_input == 6:

        print "ENTRIES LOADED"

    elif user_input == 7:
        print "Goodbye"
        break
