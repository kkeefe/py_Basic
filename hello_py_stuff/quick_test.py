#!/usr/bin/python3

# silly file to quickly test quick runs of things I make like lambdas or 
# small functions that i don't necessarily want to push everywhere..

header_count  = 0
footer_count  = 0
frame_count   = 0

# use a contents manager - passes off the resource handling..
with open('blah2.hex','r') as f:
    # store all of the contents of the file somewhere you want.
    file_contents = f.read()
# separate the contents of each item into a list by line (each element is on a new line)
words = file_contents.split('\n')
# how many lines is the data? 
word_count = len(words)
# words is a list, enumerate is a function which expands the list into 
# the number of the element we're on: count and the item we're looking at: valu
for count, val in enumerate(words):
    # do some if statements to figure out what the value is
    if val == "daa80085":
        # identify the header word
        header_count += 1
    elif val == "abaaedee":
        # identify the footer word
        footer_count += 1
    elif val == '':
        # make sure that the element we're looking at is something useful,
        # really this just ignores blank lines, like the last line of a file..
        print("blank and line: %s !" % count)
    else:
        # the data we're shipping off is split into two lines, so we want to make sure 
        # we know what half we're looking at
        frame_count += 0.5
        for nible in val:
            # the data that is read from the file is read as a string but we want that to be binary..
            # val is a string type, and this for loop looks at each letter 
            # a single letter represents four bits, which is called a 'nible'
            hex_str  = "0x" + nible       # make the format look good, and strings support addition..
            int_conv = int(hex_str , 16) 
            bin_rep  = bin(int_conv)
            print(bin_rep)                # print to make sure that the stuff we're looking at is what we want

# print overall info, header and footer counts should match, and the frame_count should be 8.5 times longer than each
print("header count: %s | footer count: % s | frame_count: %s " 
      % (header_count , footer_count , frame_count))
