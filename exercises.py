# Branching & Looping Exercises

# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')

# Write the if...elif...else statement as described in the lesson
# if color == "green":
#     print("Go!")
# elif color == "yellow":
#     print("Slow down!")
# elif color == "red":
#     print("Stop!")
# else:
#     print("Bogus!")

#  Looping Control Flow (for and while statements)
# colors = ["red", "yellow", "orange", "green"]

# for color in colors:
#     if color == "orange":
#         print("Sorry, no orange")
#     print(color)

#  looping with ranges
# let's print a range
# print(list(range(10)))

# count = int(input("Please enter count: "))

# for num in range(count):
#     print(f"Counting to: {str(num)}")

#  Practice with while statements
# count = int(input("Please enter countdown: "))

# while count > 0:
#     print(f"Counting down from {str(count)}")
#     count -= 1

# count = int(input("Please enter countdown: "))

# while count > 0:
#     print(f"Counting down from {str(count)}")
#     if count ==5:
#         break
#     count -= 1

# Wrapp this code in a While statement so that it continues to prompt the user until "quit" is entered

# color = None

# while color != quit:
#     color = input('Enter "green", "yellow", "red" or "quit": ').lower()
#     print(f'The user entered: {color}')

#     if color == "green":
#         print("Go!")
#     elif color == "yellow":
#         print("Slow down!")
#     elif color == "red":
#         print("Stop!")
#     elif color == "quit":
#         print("Exiting Process...")
#     else:
#         print("Bogus!")


#  exercise 1
# letter = input('Please enter a letter from A-Z: ').lower()
# print(f'The user entered: {letter}')

# if letter in 'a e  i  o  u':
#     print(f'The letter {letter} is a vowel!')
# else:
#     print(f'The letter {letter} is a constant')

# exercise 2
# phrase = ''
# while phrase != 'quit':
#   phrase = input('Please enter a word or phrase: ')
#   print(f'What you entered is {len(phrase)} characters long')

# exercise 3
# human_years = int(input("Input a dog's age in human years: "))
# if human_years < 3:
#   dog_years = human_years * 10
# else:
#   dog_years = 20 + (human_years - 2) * 7
# print(f"The dog's age in dog years is {dog_years}")

#  exercise 4
# print('Enter the three lengths of a triangle:')
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if a == b & b == c:
#     print(f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
# elif a != b & a != c & b != c:
#     print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
# else:
#     print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')

#  exercise 5
# term = 0
# a = 0
# b = 1

# while term < 50:
#   if term < 2:
#     print(f'term: {term} / number: {term}')
#   else:
#     num = a + b
#     print(f'term: {term} / number: {num}')
#     a = b
#     b = num
#   term += 1
    
# exercise 6
# mo = input('Enter the month of the season (Jan - Dec): ')
# day = int(input('Enter the day of the month: '))
# if mo in ('Jan', 'Feb', 'Mar'):
#   season = 'Winter'
# elif mo in ('Apr', 'May', 'Jun'):
#   season = 'Spring'
# elif mo in ('Jul', 'Aug', 'Sep'):
#   season = 'Summer'
# else:
#   season = 'Fall'
# if mo == 'Mar' and day > 19:
#   season = 'Spring'
# elif mo == 'Jun' and day > 20:
#   season = 'Summer'
# elif mo == 'Sep' and day > 21:
#   season = 'Fall'
# elif mo == 'Dec' and day > 20:
#   season = 'Winter'
# print(f'{mo} {day} is in {season}')

#  DAY 4

# Python Dictionaries 

# student = {
#     'name': 'Xavier',
#     "course": "SEIR",
#     'current_week': 12
# }

# print(type(student))

# getting value aka items in dictionary

# name = student['name']
# print(name)

# setting value aka items in dictionary
# name = student['name']

# student['name'] = 'Tina'
# student['age'] = 21

# print(student)

# USING THE GET() METHOD TO ACCESS KEYS IN A DICTIONARY
# print(student.get('location', 'Sorry this item does not exist'))

#  using the in operator with dictionary
# print('location' in student)

# student['location'] = 'Bedrock'
# print(student)

#  getting and settin values - we have to use squre bracket notation 
# dot notation is used for calling methods

#  deleting from a dictionary we use the del operator
# del student['location']
# print(student)

# finding the number of items in a dictionary
# print(len(student))

# iternating over dictionary
# for key, value in student.items():
#     print(key, value)

#  dictionary exercise
# where_my_things_are = {
#     'computer': 'on my desk',
#     'keys': 'in my pocket',
#     'car': 'in the garage'
# }

# for key, value in where_my_things_are.items():
#     print(f'{key} is kept {value}')

# LISTS
colors = ['red', 'green', 'blue']

#  get the length of a list
# print(len(colors))

#  Features of lists
#  they are ordered collections
#  they are indexed using zero
#  they are mutable
#  they are considered sequence types


#  accessing values in a list
# print(colors[0])
# print(colors[-1])

# assiging items to a list
colors[-1] = 'brown'
# print(colors)

# add items to a list
# adding one item
colors.append('purple')

# adding multiple items
colors.extend(['orange', 'black'])
# print(colors)

#  adding item to a specific position
colors.insert(1, 'yellow')

# deleting items from a list
# colors.pop(2)
color = colors.pop(2)
# print(color)

#  removing with .remove()
colors.remove('red')

#  clearing entire list
# colors.clear()
# print(colors)

# iterate over a list with a for loop
# option A - access the items only
# for color in colors:
#     print(color)

#  option B - access the items and their positions
# for idx, item in enumerate(colors):
#     print(idx, item)


#  LIST COMPREHENSIONS

# Let's create a list of squares
# with a for loop 
squares = []

nums = list(range(101))

for num in nums:
    square = num * num
    squares.append(square)

# print(squares)

# with a list comprehension
squares_alt = [n * n for n in nums]
# print(squares_alt)

#  filtering with even squares into a list

# even_squares = [n * n for n in nums if (n * n)%2 == 0]
# print(even_squares)



#  TUPLES - commas make the tuple

# phrase = ('Hello',)
# print(type(phrase))

# colors_tuple = ('red', 'green', 'blue')
# colors_tuple[0]= 'yellow'
# print(colors_tuple)

#  Tuple unpacking
# color1, color2, color3 = colors_tuple

# print(color1, color2, color3)

#  SLICING SEQUENCES
# print(colors_tuple[1::2])

# print(list(range(101))[0::2])


# PYTHON CONTAINERS LAB

# EXERCISE 1
# students = ['Xavi', 'Viv', 'Jose', 'Cali']

# print(students[1])

# print(students[-1])

# EXERCISE 2
# foods_tuple = ('pizza', 'wings', 'pita', 'tortilla')

# for food in foods_tuple:
    # print(f'{food} is a good food')

# EXERCISE 3
# for food in foods_tuple[-2:]:
#     print(food)

#  EXERCISE 4
# home_town = {
#     'city': 'new york city',
#     'state': 'new york',
#     'population': 100
# }

# print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# EXERCISE 5
# for key, value in home_town.items():
#     print(f'{key} = {value}')

# EXERCISE 6
# cohort = []
# for idx, student in enumerate(students):
#     cohort.append({'student':student, 'fav_food': foods_tuple[idx]})

# for student in cohort:
#     print(student)

# EXERCISE 7
# awesome_students = [f'{name} is awesome!' for name in students]

# for student in awesome_students:
#     print(student)

# EXERCISE 8
# for food in [food for food in foods_tuple if 'a' in food]:
#   print(food)


# DAY 5 PYTHON FUNCTIONS

# nums = [1, 2, 3, 4, 5, 6, 7]

# odds = list(filter(lambda n: n % 2, nums))
# print(odds)

#   CALLING FUNCTIONS
# def add(a,b):
#     return a + b

# def sub(a, b):
#   return a - b

# def compute(a, b, op):
#   return op(a, b)

# print(compute(1, 2, add))
#  or
# result = compute(2,2, add)
# print(result)

#  *ARGS TO ACCEPT A VARYING NUMBER OF ARGUMENS... JUST LIKE JS.. REST
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

result = add(1,2,3,4,5)

# print(result)

# **KWARGS - KEY WORD ARGUMENTS - NAME='LINDA' , AGE=21
def dev_skills(**kwargs):
    return kwargs

result = dev_skills(HTML=5, CSS=5, JS=5)

# print(result)

def dev_skills_advanced_function(dev_name, company, *args, **kwargs):
    return {
        'name': dev_name,
        'place of work': company,
        'favorite things': list(args),
        'skills': kwargs
    }

developer = dev_skills_advanced_function('Melba Mouton', 'NASA', 'Math', 'Space Exploration', 'Loved Writing Documentation', Leadership=5, Mathematics=5, Programming=5)

# print(developer)

# QUESTION 1
def sum_to(num):
    sum = 0
    for n in range(1, num + 1):
        sum += n
    return sum
# print(sum_to(5))

# QUESTION 2
def largest(nums):
    largest = 0
    for n in nums:
        if n > largest:
            largest = n
        return largest

def largest(nums):
  nums.sort()
  return nums[-1]

# QUESTION 3
def occurances(string, substr):
  # remove each occuance of substr
  stripped_string = string.replace(substr, '')
  # compute based on length of the strings
  return (len(string) - len(stripped_string)) // len(substr)
	
# Python actually has a method to solve this too!
def occurances(string, substr):
  return string.count(substr)


#  QUESTION 4
def product(*args):
    product = 1
    for n in args:
        product *= n
    return product

# print(product(2,5))




# DAY 5 PYTHON CLASSES
# class Dog():
#     def __init__(self, name, age = 0):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'His name is {self.name} and is {self.age} years old'
      
#     def bark(self):
#         return "Woof!"

# dog1 = Dog('Spot', 1)

# print(dog1.bark())

# EXERCISE - CREATE A CLASS
# 1 vin: attribute for the vehicle's identification
# 2 make: attribute for the vehicle's make
# 3 model: attribute for the vehicle's model
# 4 running: attribute for maintaining whether or not the vehicle is running. This should be set to Falsewithin the __init__method instead of being passed in at the time of instantiation.
# 5 start: method for changing runningto True
# 6 stop: method for changing runningto False

class Vehicle():
    vehicles_total = 0

    def __init__(self, vin, make, model, running):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = running
        Vehicle.vehicles_total += 1

    def __str__(self):
        return f'This is a {self.make} {self.model} with a vin of {self.vin}'
    
    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    @classmethod
    def get_total_vehicles(cls):
        return cls.vehicles_total

vehicle1 = Vehicle('ABC123', 'Tesla', 'Model S', False)
vehicle2 = Vehicle('ABC1234', 'Tesla', 'Model S', False)
vehicle3 = Vehicle('ABC12345', 'Tesla', 'Model S', False)

# print(Vehicle.get_total_vehicles())
class ExoticVehicle(Vehicle):
    def __init__(self, vin, make, model, running, top_speed = 186):
        Vehicle.__init__(self, vin, make, model, running)
        self.top_speed = top_speed

vehicle4 = ExoticVehicle('FGW345', 'Tesla', 'Roadster', False, 250)

print(vehicle4.start())
print(vehicle4.running)
print(ExoticVehicle.get_total_vehicles())