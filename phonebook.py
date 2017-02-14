import pickle


instructions = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Save entries
6. Load saved entries
7. Quit
"""
phonebook = {
    'Liette': {
        'number': '678 200 0811',
        'email': 'sample1@sample.com',
        'website': 'sample.web'},

    'Blake': {
        'number': '770 873 4404',
        'email': 'sample1@sample.com',
        'website': 'blakebagwell.com'},

    'Ashley': {
        'number': '678 922 3033',
        'email': 'sample1@sample.com',
        'website': 'sample.samplweb'}
}

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
        myfile = open('phonebook.pickle', 'r')
        phonebook = pickle.load(myfile)
        print "ENTRIES LOADED"

    elif user_input == 7:
        print "Goodbye"
        break
