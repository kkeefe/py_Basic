#!/usr/bin/python3

# silly file to quickly test quick runs of things I make like lambdas or 
# small functions that i don't necessarily want to push everywhere..

header_count = 0
footer_count  = 0
frame_count = 0

# use a contents manager - passes off the resource handling..
with open('blah2.hex','r') as f:
    file_contents = f.read()
words = file_contents.split('\n')
word_count = len(words)
for count, val in enumerate(words):
    if val == "daa80085":
        header_count += 1
    elif val == "abaaedee":
        footer_count += 1
    elif val == '':
        print("blank and line: %s !" % count)
    else:
        frame_count += 0.5
        for nible in val:
            hex_str = "0x" + nible
            int_conv = int(hex_str , 16)
            bin_rep = bin(int_conv)
            print(bin_rep)

print("header count: %s | footer count: % s | frame_count: %s " 
      % (header_count , footer_count , frame_count))
