# python ternary operator

#usefull stuff to need to enter a password :)
from getpass import getpass as gp

# 1)
# instead of:
Condition = True
if Condition:
    x = 1
else:
    x = 0
print(x)
#use:
x = 1 if Condition else 0
print(x)

# 2)
# number readability
x = 10000000000
#or
y = 10_000_000_000 #but output still won't have comma's..
z = 100_000_000
total = y + z
print(total)
# want output to have comma's?
print(f'{total:,}')

# 3) Context managers..
# instead of opening and closing files with:
f = open('blah.txt','r')
file_contents = f.read()
f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# use a contents manager - passes off the resource handling..
with open('blah.txt','r') as f:
    file_contents = f.read()
words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# 4) ---- Enumerate Function
# keeping track of a loop count:
names = ['jeff','george', 'stark','extra']
index = 0

for name in names:
    print(index, name)
    index += 1

# use the enumerate function:
for index, name in enumerate(names, start=1):
    print(index, name)

# 5) --- Zip Function
# looping through separate lists:
list_1 = ['one', 'two', 'three']
list_2 = ['boy', 'girl', 'it']

for index, name in enumerate(list_1):
    noun = list_2[index]
    print(f'{name} is actually {noun}: noun')

# use the zip function for multiple lists!
# note zip will stop at shortest list passed to it
for num, noun in zip(list_1, list_2):
    print(f'{num} is actually: {noun}')

# Note that Zip creates a tuple of the values of the lists passed to it

# 6) Unpacking
# side note: use '_' as var name for unused variables.
a, b = (1, 2)
print(a)
# print(b)
a, b, *c, d = (1, 2, 3, 4, 5) 
a, b, *_, d = (1, 2, 3, 4, 5) #this ignores c values..
# this allows a, b and d, to take the first, second and last values, respectively..

# 7) Setting Attributes to Classes

class Person:
    pass

person = Person()
person.first = 'kevin'
person.second = 'keefe'
print(person.first)

# you can instead use:
first_key = 'first'
first_val = 'val'
setattr(person,'first','kevin') # set attr can use key_vals of variable types!
setattr(person, first_key, first_val)
print(person.first)
# if there are setters, there are get attrs..
first = getattr(person,first_key)
print(first)

# example use:
person2 = Person()
person_info = {'first':'name', 'second':'last_name'}

for key, value in person_info.items():
    setattr(person2,key,value)
# print(person2.first)
# print(person2.second) # or use get attr to print

for key in person_info.keys():
    print(getattr(person2,key))

# 8 password Security
# do you like security?
Username = input("Input your username: ")
Password = gp("Input your password: ")
print('logging in..')

# 9 -- You can use 'python -m code_module' to run a particular module..

# 10 -- Helps
# help(obect)
# dir(imported_object)
# Run Python Interpreter
# Import module of interest
# help(module_name)
# can use dir(object) in the interpreter to get methods and functions of that object..
