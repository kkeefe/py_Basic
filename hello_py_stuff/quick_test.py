#!/usr/bin/python3

# silly file to quickly test quick runs of things I make like lambdas or 
# small functions that i don't necessarily want to push everywhere..

import matplotlib.pyplot as plt
import collections 

# lists = sorted(d.items()) # sorted by key, return a list of tuples
# x, y = zip(*lists) # unpack a list of pairs into two tuples
# plt.plot(x, y)
# plt.show()

# plt.plot([1,2,3,4])
# plt.ylabel('some stuff')
# plt.show()
# plt.savefig('some_stuff.png')

# # remember to set the scaler int period..
# IRS_FREQUENCY = 125_000_000
# time_in_s = int(input("give me a value of seconds "))
# time_in_ms = time_in_s / 1000

# val = ( IRS_FREQUENCY * time_in_ms ) * 2
# print(int(val))
# bin_val = hex(int(val))
# print(bin_val)

# -- verify scaler reading -- #
IRS_SCALER_VAL = 0x2000
# get_scaler = lambda x: (IRS_SCALER_VAL | x << 2)
# pixel_scaler_map = {}
# for pixel in range(0, 64):
#     pixel_scaler_map[pixel] = get_scaler(pixel)
# for pix , addr in pixel_scaler_map.items():
#     print(pix, hex(addr), bin(addr))

# lets try creating a class to store this data
class Scan_Data():
    def __init__(self, data_list=[]):
        self.data_list = data_list
    
    def add_data(self, x_y_val={}):
        self.data_list.append(x_y_val)
class Pixel_Data():
    def __init__(self, pixel_number):
        self.number = pixel_number
        self.data   = Scan_Data()
    def set_data(self, data=Scan_Data()):
        self.data = data

# lets create a data object that we want to dump into a file.
total_pixel_data =  [] # fundamental list type object

# lets create 64 places of pixel data!
for i in range(0,64):
    pix = Pixel_Data(i)
    total_pixel_data.append(pix)

# lets fill the Pixel_Data values and then attribute them to Scan_Data
# this creates a single particular scan value to add to one particular pixel..
thresh_min = 3000
thresh_max = 3500
scan1  = Scan_Data()
for i in range(thresh_min, thresh_max):
    data_point   = {}
    thresh_val   = i
    scaler_count = i*i
    data_point[thresh_val] = scaler_count
    scan1.add_data(data_point)
    # find the pixel this corresponds to and add it 
    for item in total_pixel_data:
        if i == item.number:
            item.set_data(scan1)

for pixel in total_pixel_data:
    f = open("test_dir/pixel_%s.txt" % pixel.number, "w")
    f.write("pixel\tthresh\t scaler_count")
    for point in pixel.data.data_list:
        f.write("\n")
        for key, value in point.items():
            f.write("%s\t%s \t %s" % (pixel.number , key , value) )
    f.close()

# sexy things suggested on stack exchange:

# for key in mydictionary:
#    print "key: %s , value: %s" % (key, mydictionary[key])

# keys = mydictionary.keys()
# keys.sort()

# for each in keys:
#     print "%s: %s" % (each, mydictionary.get(each))

# # lets do some file things
# for j in range(0,10):
#     f = open("test_dir/test_file%s.txt" % j,"w")
#     for i in range(0,10):
#         f.write("hi there\n")
# f.close()

# after the stuff is in the file we want to be able to retrieve it at a different time 
# it would be nice if we could maybe read this data and plot it?