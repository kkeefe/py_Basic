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

# lets do some file things
for j in range(0,10):
    f = open("test_file%s.txt" % j,"w")
    for i in range(0,10):
        f.write("hi there\n")
f.close()