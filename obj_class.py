#1 Basics

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greetingCount = 0
        self.uniqueGreeting = set()

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greetingCount += 1
        self.uniqueGreeting.add(other_person)

    def print_contact_info(self,):
        print "%s's email: %s. %s's number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print len(self.friends)

    def __repr__(self):
        return '<Person %s %s %s>' % (self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print len(self.uniqueGreeting)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

print "%s's email: %s. %s's number: %s" % (sonny.name, sonny.email, sonny.name, sonny.phone)

print "%s's email: %s. %s's number: %s" % (jordan.name, jordan.email, jordan.name, jordan.phone)

#2 Make your own class

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info():
        print "%s %s %s" % (self.year, self.make, self.model)


sonny.greet(jordan)
sonny.greet(jordan)

sonny.num_unique_people_greeted()
