
        attributes like - 'fertility' that is a determines breeding success rate

        stage one:
          create dictionaries with content of numerous animal qualities

          create a function that randomly picks a quality of of each category and appends it to a list. the list being all the chosen qualities for an animal

          have a the system output a sentence talking about each of the qualities that the creature has


      Stage 2:
      save creature function
      auto load creatures

      name creature(attribute)

      allow a person to get info about their creature again, without having to create a new one.

      implement a menu that lets them 'create' 'look at previous creations'
            if look at previous creations
              give the option to view traits
              or destroy
                if destroy:
                  ask for confirmation
                    if yes
                      delete


      create a new method for creatures thats allows breeding with other creatures, and that will make a new creature with random traits, but only the traits pulled from its parents.

      if choice == 1:
          while:
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
                break

      if choice == 2:
          #select a creature
          #menu of all creatures in zoo
          #use a loop
          for i in zoo:
              print i ' >-- ' creature
          #now as for user inputs
            if 
      if choice == 3:
          print 'You question your ethics...'
          break#quit the game
      else:
        print 'invalid input'
