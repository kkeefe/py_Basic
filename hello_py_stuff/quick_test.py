#!/usr/bin/python3

# silly file to quickly test quick runs of things I make like lambdas or 
# small functions that i don't necessarily want to push everywhere..

# lets try making some nice user interface stuff
# but lets make sure we handle stupid user input first..

# errors from user input not giving you the int value you want..
running = True
while running:
    try:
        user_input = int(input("please enter somethign you want to do.."))
        running = False
    except ValueError:
        print("you did not enter an integer..")
        running = True
    # this prevents Ctr-C from exiting the program..
    except KeyboardInterrupt:
        print("you tryna leave mate?")

def myFunc(arg1 , arg2):
    assert(arg2 != 0), "you don't want to divide by 0"
    return arg1 / arg2

# assertion errors from functions.
running = True
while running:
    try:
        user_input = int(input("please enter some integer to divide by.."))
        myFunc(5,user_input)
        running = False
    except AssertionError:
        running = True
        print("what the fuck are you thinkin dividing by zero?")

# lets try some standard file I/O errors..
running = True
while running:
    try:
        file_name = input("please enter the name of the file you want to read from: ")
        with open(file_name, 'r') as f:
            print("hey you opened the file.")
            contents      = f.read()
        running = False
    # this exception occurs if the file to read does not exist.
    except IOError:
        print("son, that doesn't fuckin exist.\nTry that shit again..")
        running = True

# x in contents is every single value in the file
for val, x in enumerate(contents):
    print(val, x)

# lets see what happens if we test your user input against int values..
val = 5
try:
    print(user_input + val)
except TypeError:
    print("you did not enter an int value..")