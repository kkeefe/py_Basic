# Chapter 1...
# message = "hello worlds!"
# print(message)

# message = "hello worlds! two"
# print(message)

# use pound for a comment
# common tools on strings: title(), upper(), lower(), [r][l]strip() to remove whitespace..
# strings also obey the addition rules you would expect..
# name = "title author"
# print(name.title())

#Chapter 2...
#make sure to use str(arg) when you want to type_cast something to print it to output..
#note that python2 and python3 do not handle int divison the same.. python2 will force rounded down int answer
# int_5 = 5
# message_2 = message + str(int_5)
# print(message_2)

# #this would have an error if the variable was closed with single quotes..
# message = "One of Python's strengths is its diverse community."
# print(message)

# you may type 'import this' -no quotes to print The Zen of Python (?)

#Chapter 3... Lists..
Numbers = ["one", "two", "three"]
# print(Numbers)
# # notes: Numbers can be element accessed like so:
# print(Numbers[0])
# print(Numbers[-1]) #negative numbers will reverse wrap.. in fact this always returns last element in list, otherwise for empty list returns error

# think of indexing the list as accessing that element directly, and you can change its value through assignments..
# use .append(element) to add elements to a list..

# note a count() function could return the number of times an element appears in a list
# list.count(element) {returns an int}

# or you can use insert to put it in a particular spot within the list..
# Numbers.insert(1, "four")
# print(Numbers)

# use del to remove elements..
# del Numbers[1]
# print(Numbers)

# similarly, you can remove and return a value from a list in any position with .pop(pos)..
# or.. remove('value') from the list.. #note that this only removes the first occurance of value within list..

#list misc:
# list.sort() #this will rank order elements of the list through comparison operators..
# list.sort(reverse=True) #this will rank order in reverse..
# list.reverse() #reverse the order of the list..
# len(list) #return an int for the length of the list..

# # ch 4  for loops, notice here that the for loop, or the scope of it, is determined by the indentation..
# # note that this is the first example of python indentation, notice that the only thing that matters for the scope of the for loop is that the minimum level of indentation be matched..
# for num in Numbers:
#     print(num)
#     print(num)

# #note that the below for loop will not print 5, this also introduces the range function..
# for value in range(1,5):
#     print(value)

# #note that the below will print the list, not the individual elements within the list..
# ints = list(range(1,5))
# print(ints)
# print(ints[1:4])

# #empty list declaration and use..
# self_pow = []
# for val in range(1,10):
#     square = val**val
#     self_pow.append(square)
# print(self_pow)

#useful math functions: sum(list), max(), or min() could be useful..
#print(sum(self_pow))
# note that this range list reads: from 3 to 30 by increments of 3, note that 31 is needed to ensure that 30 is included in the list..
# mult_3 = list(range(3,31,3))
# print(mult_3)

# #tuple types in python do not want to be changed:
# dimensions = tuple(range(1, 10, 2))
# print(dimensions)
# print(dimensions[1])
# error: tuple does not support item assignment:
# dimensions[1] = 2

#Ch5:If statements and for loops
# for value in self_pow:
#     #note the syntax of an if statement: if (condition) : <statements>
#     if value == 1 or value == 256:
#         print("value is: " + str(value))
#     elif value == 4:
#         print("value is: " + str(value))
#     #note python does not require else statements to conclude if statements..
#     else:
#         print(str(value) + " is not 1")

# # check to see if in a list
# person_list = ['john', 'kelly']
# person_name = 'john'
# if person_name in person_list:
#     print(person_name)

#example of conditional statements in list:
# <item> in <list> -> return value is boolean
# may also pay boolean arguments to print() to return True/False string values..
# for lists, an if condition can test to see if the list is empty, i.e.: if list: <statements>

#Ch6: Dictionaries-
# A dictionary is a dynamic object which is a ex of key-value pairs,
# initialize:
# dic = {'key1' : 'green', 'key2' : 'blue'}
# print(dic)
# # add to
# dic['key3'] = 'red'
# print(dic)
# # remove from
# del dic['key1']
# print(dic)
# # loop through it
# for key, value in dic.items():
#     print("key is: " + str(key))
#     print("value is: " + str(value))

# # select the keys..  .values() also works well..
# for key in dic.keys():
#     print("key is: " + str(key))
# # # get the keys you want in order
# for key in sorted(dic.keys()):
#     print("key is: " + str(key))

# Nesting: storing lists in dictionaries, or any combination therein.

#Ch7: User input and while loops
#input() function requests user input..
# message = input("tell me the thing you want me to answer: ")
# print(message) # this will print the value you just entered to input..

# #if you want to enter an integer you'll need to recast the input with int():
# message = input("tell me how old you are: ")
# message = int(message)
# print(message)

# the modulo operator - returns the remainder of the division between two int types

# #while loops - ideal to iterate through lists and dictionaries where modification is required
# # avoid iterating through lists / dicts with for loops: python no like
# val = 0;
# while val < 5:
#     print(val)
#     val += 1

# #flags and while loops: (continue and break)
# active_flag = True
# while active_flag:
#     response = input("give me a response: ")
#     if response != "quit":
#         print("enter quit to leave..")
          # could include a break here to immediately leave the loop..
#     else:
#         active_flag = False
          # could also include a continue line to immediately move to the next iteration of the while loop..

# # while loops with lists and dictionaries -
# foods = ["pizza", "burritos", "tacos"]
# foods_i_like = []
# # go through every element in foods..
# while foods:
#     food = foods.pop() #pop is a useful feature to randomly remove any element from a list and then perform some checks on it..
#     print("adding: " + food)
#     foods_i_like.append(food)
# print("the foods i like are:")
# print(foods_i_like)

# foods_i_like.append("tacos") #add another element to it
# print("the foods i like are:")
# print(foods_i_like)

# while "tacos" in foods_i_like:
#     foods_i_like.remove("tacos")
# print("the foods i like are:")
# print(foods_i_like)

#Ch8: Functions -
#Syntax -> Def function_name(parameter list)
#               -> function_things
#               -> optional specify return type..
# def display_message():
#     print("hi there..")
# #remember the function call!!!
# display_message()

#positional arguments vs. Keyword arguments:
# -> positional arguments are simply the normal ordering of arguments..
# -> keyword arguement: name, value pair passed to a function
# -> Default arguments
# def function_stuff(arg1, arg2="ni hao"): #nondefault arguments must go first..
#     print(arg1)
#     print(arg2)
# function_stuff("hello", "hi") #positional arguments
# function_stuff(arg1="hi", arg2="hello") #keyword arguements
# function_stuff("great") #default argument for arg2..

#may specify return values from a function. you can use function for assignments..
#arg2 / 3 are optional parameters..
def lets_do_math(arg1, arg2=0, arg3="add"):
    val = arg1 + arg2
    if arg3 == "add":
        print("adding: ")
        return val + arg1
    elif arg3 == "subtract":
        print("subtracting: ")
        return val - arg1
    else:
        print("this form of math is unknown!!")
        return 0

add = lets_do_math(2,1,"add") #equivalent to lets_do_math(2,1)
subtract = lets_do_math(2,1,"subtract")

# # rusing functions and returning disctionary types
def make_element(element_name, element_number, element_mass):
    """create an element dictionary"""
    element = {'name':element_name, 'number':element_number, 'mass':element_mass}
    #since no element_list is passed to here, use this function to create / return one.
    return element

#pass a list and a dictionary to a function
def add_element(element_list, element):
    """stuff which describes a function,
       feel free to put it on multiple lines.. lists and dictionaries passed to functions can
       be modified inside of that function.."""
    if element:
        print("adding element to list!")
        element_list.append(element)

#make a new element list, from a passed dictionary
def make_element_list():
    """use user input to create an element list, since this function requires no list to be
    passed to it, the function creates and return it's own function, hence 'create_list'"""
    element_list = []
    more_elements = True

    while more_elements:
        usr_response = input("do you have more elements to add? (yes to add) ")
        if usr_response=="yes":
            name = input("please input the element name: ")
            number = input("please input the element number: ")
            mass = input("please input the element mass: ")
            #use a function call inside of another function
            add_element(element_list, make_element(name, int(number), float(mass)))
        else:
            print("thanks for your elements! ")
            more_elements=False

    return element_list

# call the function and print below:
# element_list = create_element_list()
# print(element_list)

#send copies of lists to a function list[:] - known as 'slice notation'

#Functions with arbitrary number of arguments..
def print_things(*arg1): #this will tell python to make an empty tuple for arg1
    """tuples are like lists, but immutable and hence don't like modified"""
    print(arg1)
    for val1 in arg1:
        print("- " + val1)
print_things("things1", "things2")

#you can also have an arbirarily long dictionary passed to a function:
def print_things_d(**arg1):
    """dictionary types have key values, so you want to make sure you capture them all"""
    thing_d = {}
    for key, value in arg1.items():
        thing_d[key] = value
    #things the dictionary you just passed.
    print(thing_d)
dic_1 = {'val1' : 1, 'val2' : 2}
print_things_d(val1=1,val2=2)

#Ch9: Classes -

# typical example of defining a class and the initalizer for the class..
class element():
    def __init__ (self, name, number, mass):
        self.name = name
        self.number = number
        self.mass = mass
    # lets get some functions
    def get_stats(self):
        print(f'name: {self.name}\nnumber: {self.number}\nmass: {self.mass}')
# lets create an example of this basic class
ele_A = element('hydrogen', 1, 1.0079)

# and use a member function!
ele_A.get_stats()

# since the class chapter is likely the be crucial, it might be worthwile to quickly do every excercise in this chapter..

#Ex: 9.1 -
class Restaurant():

    def __init__ (self, name, cuisine_type):
        self.name = name
        self.food_type = cuisine_type
        #9.5 
        self.num_served = 0

    def describe_restaurant(self):
        print(f'name: {self.name}\nfood type: {self.food_type}\nnum served: {self.num_served}')

    def open_restaurant(self):
        print("the place is open!")

    def set_num_served(self, num):
        self.num_served = num
        print(f'num serverd is: {self.num_served}')

    def inc_num_served(self):
        self.num_served += 1

# rest_1 = Restaurant("Mickie-D's", "Fast Food")
# rest_1.describe_restaurant()
# rest_1.open_restaurant()

# #Ex: 9.2 - Create three instances from the class above..
# rest_2 = Restaurant("Arbies", "Fast Food")
# rest_2.describe_restaurant()
# rest_3 = Restaurant("Burger King", "Fast Food")
# rest_3.describe_restaurant()
# rest_4 = Restaurant("Shaloha", "Greatness")
# rest_4.describe_restaurant()

#Ex: 9.3 - make a user class that includes first and last name, as well
# as other information that a user might want to include..
class User():

    def __init__(self, first_name, last_name, password, age):
        """basic initializer method.."""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """print the user attributes line by line.."""
        print(f'first name: {self.first_name}')
        print(f'last name: {self.last_name}')
        print(f'password: {self.password}')
        print(f'age: {self.age}')

    def greet_user(self):
        """boring generic greeting"""
        print(f'ni hao, {self.first_name}!')
        self.inc_login_attempts()

    def get_login_attempts(self):
        """how many times has this user tried to log in?"""
        print(f'number of login attempts: {self.login_attempts}')

    def inc_login_attempts(self):
        """#everytime the user is greeted, they have logged in.."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset it to zero.."""
        self.login_attempts = 0


first_user = User('kevin', 'keefe', 'blank', 28)
first_user.greet_user()
first_user.describe_user()

# annoyingly you can also add random things to your class..
first_user.stuff = "hi there"
print(first_user.stuff)

# ex 9.4
rest1 = Restaurant("place1", "bad_food")
rest1.set_num_served(5)
rest1.inc_num_served()
rest1.describe_restaurant()

# # ex 9.5 - set a user log in attempt method and call it
# first_user.get_login_attempts()
# first_user.reset_login_attempts()
# first_user.get_login_attempts()

# # inheritance!
# # Child classes inherit all methods and attributes of the parent class..

# # make a child class of the restaurant class for ice cream!

# class Ice_Cream_Stand(Restaurant):
#     def __init__(self, name, cuisine_type="Ice Cream", flavors=[]):
#         super().__init__(name,cuisine_type)
#         self.flavors = flavors

#     def get_flavors(self):
#         if self.flavors:
#             print(f'flavors are: {self.flavors}')
#         else:
#             print("please input some flavors!")

# eddies = Ice_Cream_Stand("eddies")
# eddies.describe_restaurant()
# eddies.get_flavors()

# # create a separate privileges class.
# class Privileges():
#     def __init__(self, attribute=[]):
#         self.attribute = attribute

#     def set_privileges(self):
#         count = int(input("How many privileges do you wish to set for the user?"))
#         while count != 0:
#             privilege = input("please add a privilege: ")
#             self.attribute.append(privilege)
#             count = count - 1

#     def show_privileges(self):
#         print(self.attribute)

#     def check_privilege(self, priv):
#         # quickest and clearest way to check to see if a particular element
#         # is in a list!
#         if priv in self.attribute:
#             print("got it!")
#         else:
#             print("nope!")


# class Admin(User):

#     def __init__(self, first_name, last_name, password, age):
#         # this method calls all of the initializations of the parent class..
#         super().__init__(first_name, last_name, password, age)
#         #extension of 9.6 / 9.7 to make a class an attribute..
#         self.privileges = Privileges()

#     def display_privileges(self):
#         if self.privileges.attribute:
#             print(f'Privileges for {self.first_name} are: {self.privileges.show_privileges()}')
#         else:
#             print("please input some priviledges for user.")

# admin1 = Admin(first_user.first_name, first_user.last_name, first_user.password, first_user.age)
# admin1.display_privileges()
# admin1.privileges.set_privileges()
# admin1.privileges.show_privileges()

# # altering exercise 9.9 since it requires to write out all of car / electric car / battery class..
# # instead will create a method to check priviledges inside of Admin class for 'set password'
# check_priv = input("input the privilege you want to check for: ")
# admin1.privileges.check_privilege(check_priv)

# No examples for the next three exercises since they're exceptionally trivial..
# Ex 9-10 : store a class in a module and import it. Use that module in your local copy.
# Particularly do this for the restuarants class..

# Ex 9-11 : Do the same as the above exercise except put the User and Admin classes
# in a separate module..

# Ex 9-12 : Do the same as above except put user in one module, with admin in a different one
# run some commands to make sure that everything is imported correctly..

# Importing collections and other modules from the standard library..

# import collections

# # example of importing and using an ordered dictionary..
# order_dic = collections.OrderedDict()
# order_dic = {'stuff':'thing'}
# print(order_dic)

# # Ex 9-13 : Make an ordered dic and ensure that the print output matches the input value
# count = 3
# while count != 0:
#     count = count - 1
#     value = input("add another thing to the dicionary!")
#     order_dic[count] = value
# print(order_dic

# Ex 9-14 : Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1-# of sides
import random

class Die():

    def __init__(self, side_num=6):
        Die.sides = side_num

    def roll_dice(self, display=False):
        val = random.randint(1,self.sides)
        if display:
            print('value of the die toss is: %s' % val)
        return val

six_side = Die(6)
six_side.roll_dice(display=True)

# chapter 15 stuff - data visualization

# get some mat plot lib stuff
import matplotlib.pyplot as plt

# do some basic plotting of a generic list
squares = [1,2,3]
squares_val = [1,4,9]

plt.title("title goes here", fontsize=24)
plt.xlabel("x axis label here")
plt.ylabel("y label here, i guess")
plt.plot(squares, linewidth=5)
plt.show()

# # give x and y vals if you wish..
# plt.axis([0,10,0,10])
# plt.plot(squares, squares_val, linewidth=3)
# plt.show()

# scatter plots and the random module

from random import choice
class RandomWalk():
    """
    all stuff below stolen directly from textbook..
    """
    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points :

            # set up the function which defines changing x / y distances.
            x_direction = choice([-1,1])
            x_distance  = choice([0,1,2,3,4])
            x_step      = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance  = choice([0,1,2,3,4])
            y_step      = y_direction * y_distance

            # dont stop if both zero
            if x_step == 0 and y_step == 0:
                continue

            # find the last values and increment from there.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # add those values into the list.
            self.x_values.append(next_x)
            self.y_values.append(next_y)

# make some random walks happen and show it!
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

# want to color it as you go along?
point_numbers = list(range(rw.num_points))
# ignore error to below.. plotlib does infact have this member..
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

# get the start and end values specially..
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
plt.show()

# histograms in python
import pygal
hist = pygal.Bar()

hist.title = "hist title"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title  = "Result"
hist.y_title  = "Frequency of Result"

# lets get some data
results =[]
for roll_num in range(1000):
    result = six_side.roll_dice()
    results.append(result)

# lets get some frequencies
frequencies = []
for val_i in range(1, six_side.sides+1):
    frequency = results.count(val_i)
    frequencies.append(frequency)

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

# #additional neat things learned on the side:
# # lets get the operating system..
# import os
# import sys
# # this allows access to any of the operating system
# # values.. environ_values is set to be a dictionary, with key : value types
# #..
# environ_values = os.environ
# print(environ_values)
# print("\n")
# print(environ_values['os'])

# sys_values = os.sys
# print(sys_values)

