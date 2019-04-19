#!/usr/bin/python3

import sys
import lappd
import socket
from random import randint

import collections 

IRS_REGRST_ADDR   = 0x1030
IRS_OFFSET_ADDR   = 0x4000
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

# keefe added registers..
IRS_ITCHY_SCRATCHY = 0x0020
IRS_DATA_AFT       = 0x1000 # toggles data_en off
IRS_DATA_BEF       = 0x1004 # data_en off 
IRS_SOFT_TRIG      = 0x1028 # toggles data_en on
IRS_SCALER_PRD     = 0x1100 
IRS_NBIC_PORTS     = 0x0218

if len(sys.argv) < 2:
    print("Usage: %s <broadcast address>" % sys.argv[0], file=sys.stderr)
    exit(1)

print("")
print("IRS python interface test stub")
print("----------------------------------")

# # find all of the boards on the network
my_boards = lappd.discover(sys.argv[1])

# do soem stuff to the boards, but will likely be only doing this to the IRS board..
for board in my_boards:

    # print the boards you're connected too
    print("Connected to board: %s @ %s\n-------------------------" % 
        (board.dna.hex(), board.dest))
    # It should be pointing to the gateway
    maclow = board.peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTMAC_LOW)
    machigh = board.peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTMAC_HIGH)

    print("Board %s NBIC target MAC low: %s, high: %s" % (board.dna.hex(), hex(maclow), hex(machigh)))

    # # do we need to do a register reset? who knows.
    # input("Press Enter to initiate register reset...")
    # board.pokenow( IRS_REGRST_ADDR , 0x1 )
    # print("...done.")

    input("Aiming at self...")
    board.aimNBIC()

    # Lets confirm that its stored in big endian order
    result = board.peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTIP)

    # If it is, this will print out the bytes reversed, since it expects
    # little endian
    print("Dest IP: %s" % hex(result))

    # these values below try to attempt a reg value set..
    # input("lets try some itchy_scratchy reading and writing..")
    # board.pokenow( 0x0020, 0xf )
    # result = board.peeknow( 0x0020 )
    # print("value from  the itchy read is: %s" % hex(result))

    input("lets trying writing to data_addr_bef")
    board.pokenow( IRS_DATA_BEF , 0x1 )
    result = board.peeknow( IRS_DATA_BEF )
    print("value from data_addr_bef is: %s" % hex(result))

    input("lets trying writing to data_addr_aft:")
    board.pokenow( IRS_DATA_AFT, 0x1 )
    result = board.peeknow( IRS_DATA_AFT )
    print("value from data_addr_aft: %s" % hex(result))

    input("lets read the UDP source(low byte ) and dest ports(high byte)..")
    result = board.peeknow( IRS_NBIC_PORTS )
    print("value from data_addr_aft: %s" % hex(result))
    
    input("lets try writing to the scaler_period..")
    board.pokenow( IRS_SCALER_PRD, 0xfffe )
    result = board.peeknow( IRS_SCALER_PRD )
    print("value from data_addr_aft: %s" % hex(result))

    input("lets attempt a software trigger! Soft register is a read only reg.. Reads evtNumber: ")
    result = board.peeknow( IRS_SOFT_TRIG) # note this also sets read_data_enable to FSM..
    print("value read from the software trig: %s" % hex(result))
    result = board.pokenow( IRS_SOFT_TRIG , 0xf ) # note this also sets read_data_enable to FSM..

    # input("lets attempt a software trig with a peek value.. ")
    # board.peek( IRS_SOFT_TRIG ) # note this also sets read_data_enable to FSM..
    # board.poke( IRS_SOFT_TRIG , 0xf )
    # input("press enter to commenct the transact.")
    # board.transact()
    

    # IRS_OFFSET_JUMP   = 0x0100 << 2 # same thing as multiply by four..
    # IRS_OFFSET_ADDR   = 0x4000

    # asic = lambda x,y : (IRS_OFFSET_ADDR | y * IRS_OFFSET_JUMP | x)

    # # print("next, or the values....")
    # # print(hex(IRS_OFFSET_JUMP))

    # asic_dac = lambda x: bin(( IRS_OFFSET_ADDR | x << 2))
    # hex_asic_dac = lambda x: hex(( IRS_OFFSET_ADDR | x << 2))
    # asic_dac_dic = {asic_dac(x): 0x0 for x in range(0,64)}

    # for count, x in enumerate(range(0,64)):
    #     print(count,asic_dac(x),hex_asic_dac(x))
    # # print(asic_dac_dic)

    # print("next lambda, asic..")
    # print(hex(asic(1,2)))