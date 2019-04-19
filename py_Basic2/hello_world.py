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
# use .appent(element) to add elements to a list..

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
# A dictionary is a dynamic object which is a collection of key-value pairs,
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
def display_message():
    print("hi there..")
#remember the function call!!!
display_message()

#positional arguments vs. Keyword arguments:
# -> positional arguments are simply the normal ordering of arguments..
# -> keyword arguement: name, value pair passed to a function
# -> Default arguments
def function_stuff(arg1, arg2="ni hao"): #nondefault arguments must go first..
    print(arg1)
    print(arg2)
function_stuff("hello", "hi") #positional arguments
function_stuff(arg1="hi", arg2="hello") #keyword arguements
function_stuff("great") #default argument for arg2..

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

#using functions and returning disctionary types
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

rest_1 = Restaurant("Mickie-D's", "Fast Food")
rest_1.describe_restaurant()
rest_1.open_restaurant()

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

# ex 9.5 - set a user log in attempt method and call it
first_user.get_login_attempts()
first_user.reset_login_attempts()
first_user.get_login_attempts()


# inheritance! 
# Child classes inherit all methods and attributes of the parent class..

# #additional neat things learned on the side:
# # lets get the operating system..
# import os
# import sys
# # this allows access to any of the operating system values.. environ_values is set to be a dictionary, with key : value types..
# environ_values = os.environ
# print(environ_values)
# print("\n")
# print(environ_values['os'])

# sys_values = os.sys
# print(sys_values)

