#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

print "I will now count my chickens:"

# prints Hens 30
print "Hens", 25 + 30 / 6
# prints Roosters 97
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# prints 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# prints False
print 3 + 2 < 5 - 7

# prints What is 3 + 2? 5
print "What is 3 + 2?", 3 + 2
# prints What is 5-7? -2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

# prints Is it greater? True
print "Is it greater?", 5 > -2
# prints Is it greater or equal? True
print "Is it greater or equal?", 5 >= -2
# prints Is it less or equal? False
print "Is it less or equal?", 5 <= -2

#PART II

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints all the days
print "Here are the days: ", days
# prints all the monts on new lines
print "Here are the months: ", months

#PART III

# creates an array of numbers
the_count = [1, 2, 3, 4, 5]
# creates an array of strings
fruits = ['apples', 'oranges', 'pears', 'apricots']
# creates an array of strings and numbers
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# loops through the_count and
# prints all the numbers from the_count for %d
for number in the_count:
    print "This is count %d" % number

# loops through fruits and 
# prints all the fruits from fruits for %s
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Loops through change and prints all of its contents
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# loops the variable i from 0 to 6 and adds it to the list elements
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# loops through all elements in elements and prints them
for i in elements:
    print "Element was: %d" % i



#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I
ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "The 'stuff' list: ", stuff

# prints the second element, Oranges
print stuff[1]
# prints the last element, Corn
print stuff[-1]
# pops Corn off the stuff list 
print stuff.pop()
# prints the stuff list in a single line with each word seperated by a space
print ' '.join(stuff) 
# prints items 3 and 4 from the stuff list seperated by #
print '#'.join(stuff[3:5]) 

#PART II

#Create comments where marked with # to explain the code below

# creates a dictionary that maps the states with their abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# creates a dictionary that maps the abbreviations with cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# sets the key NY to New York in the cities dictionary
cities['NY'] = 'New York'
# sets the key OR to Portland in the cities dictionary
cities['OR'] = 'Portland'

# prints - 10 times
print '-' * 10
# prints NY State has: New York
print "NY State has: ", cities['NY']
# prints OR State has: Portland
print "OR State has: ", cities['OR']

# prints - 10 times
print '-' * 10
# prints Michigan's abbreviation is: MI 
print "Michigan's abbreviation is: ", states['Michigan']
# prints Florida's abbreviation is: FL
print "Florida's abbreviation is: ", states['Florida']

# prints - 10 times
print '-' * 10
# prints Michigan has: Detroit
print "Michigan has: ", cities[states['Michigan']]
# prints Florida has: Jacksonville
print "Florida has: ", cities[states['Florida']]

# prints - 10 times
print '-' * 10
# stores the key in state and the value in abbrev
# loops through states dictionary and prints all items
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# prints - 10 times
print '-' * 10
# stores the key in abbrev and the value in city
# loops through cities dictionary and prints all items 
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# prints - 10 times
print '-' * 10
# stores the key in state and the value in abbrev
# loops through states dictionary and prints all items
# also prints all the values in cities baesd on the key abbrev
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])


