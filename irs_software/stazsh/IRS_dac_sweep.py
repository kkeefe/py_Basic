# !/usr/bin/python3

import sys
import lappd
import socket
from random import randint

import time
import collections 

IRS_REGRST_ADDR   = 0x1030
IRS_OFFSET_ADDR   = 0x4000 #address for the ASIC's dacs..
IRS_OFFSET_JUMP   = 0x0100 << 2
IRS_THRESH_OFFSET = (129-1) << 2
IRS_VOFS1_OFFSET  = (130-1) << 2
IRS_VOFS2_OFFSET  = (131-1) << 2
IRS_CHANNEL_JUMP  = 0x4 << 2
IRS_WBIAS_OFFSET  = (132-1) << 2
IRS_DIGREG_ADDR   = (169-1) << 2
IRS_TBBIAS_ADDR   = (161-1) << 2
IRS_ITBIAS_ADDR   = (164-1) << 2
IRS_VBIAS_ADDR    = (162-1) << 2
IRS_VBIAS2_ADDR   = (163-1) << 2

# asic_dac has 12 bit write value
# asic_dac has a 32 bit read value

# ADDR to write to
IRS_OFFSET_ADDR = 0x4000 # note firmware technically only reads top two bits of highest byte
#in Hz
IRS_FREQUENCY = 125_000_000

# ADDR to read from
IRS_SCALER_PRD    = 0x2000 

# lets use the integration time that we've set up!
int_time = int(input("how long do you want the int period to be?"))
def integration_time(int_time):
    """
    this defines how long program should wait before issuing another
    value to read or write from the IRS
    """
    seconds = int_time * IRS_FREQUENCY
    scaler_int_pd = bin(seconds)
    print(f'scaler binary rep is: {scaler_int_pd}')
    print(f"lets wait {seconds} seconds before seeing the result.")

    time.sleep(seconds)

def read_scaler_count(board):
    """
    this function reads out all of the scaler counts from each pixel.
    It will return the addresses and the scaler count for each picture in a dictionary
    type.
    """

    # create the register map for the dic type
    hex_scalar_val = lambda x: hex(( IRS_SCALER_PRD | x << 2))

    # this is creates the dictionary of all of the register addresses as key values.
    # poke each of the registers you want during the initialization of this dictionary type
    asic_scalar_dic = {hex_scalar_val(x) : board.peeknow(hex_scalar_val(x)) for x in range(0,64)}

    return asic_scalar_dic

def IRS_dac_sweep(board, dacADDR):
    """
    this function will attempt to poke the same register with
    every bit value 11:0..
    """
    print("sweeping all ASICs on all Channels..")
    for value in range(0x0, 0xfff):
        board.pokenow( dacADDR , value )    


bin_asic_dac = lambda x: bin(( IRS_SCALER_PRD | x << 2))
hex_asic_dac = lambda x: hex(( IRS_SCALER_PRD | x << 2))

# this is creates the dictionary of all of the register addresses as key values.
asic_dac_dic = {hex_asic_dac(x): 0x0 for x in range(0,64)}

print(asic_dac_dic)

# lets see to make sure that all of the values we want are actually coming out..
# this will define the iterative read we want from all of the scalers on the pixels
for count, x in enumerate(range(0,64)):
    print(count,bin_asic_dac(x),hex_asic_dac(x))



# IRS_OFFSET_JUMP   = 0x0100 << 2
# IRS_VBIAS_ADDR    = (162-1) << 2
# IRS_VBIAS2_ADDR   = (163-1) << 2

# asic = lambda x : hex(IRS_OFFSET_ADDR | y * IRS_OFFSET_JUMP | x)

# # Initializing some things to zero
# regmap = { asic(x) : 0x0 for x in (IRS_VBIAS_ADDR, IRS_VBIAS2_ADDR) }

# print(regmap)
# print(f'{IRS_OFFSET_JUMP} is offset jump')