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

def configIrsTrigger(board, asicNum):
    
    ############################# THE NEW WAY
    # First, define an anonymous function which applies the common offset we care about.
    # (the parenthesis after : are not required, but they make the syntax more clear
    #  to n00bs)
    asic = lambda x : (IRS_OFFSET_ADDR | asicNum * IRS_OFFSET_JUMP | x)

    # Initializing some things to zero
    regmap = { asic(x) : 0x0 for x in (IRS_VBIAS_ADDR, IRS_VBIAS2_ADDR) }
    
    # Note that regmap is a dict() type, it links keys (reg addrs) to values (words)
    # dict() is unordered for Python < 3.7, so these register assignments need not happen
    # in the order they are written into the Python.

    # Now explicitly set things that are non-zero
    # This will create entries in the regmap, as necessary, or reassign them if they
    # already exist.
    regmap[asic(IRS_ITBIAS_ADDR)] = 1300
    regmap[asic(IRS_TBBIAS_ADDR)] = 1300
    regmap[asic(IRS_DIGREG_ADDR)] = 5

    # If we need to guarantee that register transactions happen in the order in which they are set,
    # we need to use an ordered dictionary.  This will iterate in the order FIRST assigned.
    # Reassignments do not mutate order.
    #
    # This is the Python standard collections framework
    o_regmap = collections.OrderedDict()
    
    # Channel specific registers
    for chanNum in range(0,8):
        # Again, define an anonymous function which applies the common offset for this channel
        chan = lambda x : (IRS_CHANNEL_JUMP * chanNum | x)
        
        # Set the registers
        o_regmap[asic(chan(IRS_WBIAS_OFFSET))] = 1300
        o_regmap[asic(chan(IRS_VOFS1_OFFSET))] = 1500
        o_regmap[asic(chan(IRS_VOFS2_OFFSET))] = 2000
        o_regmap[asic(chan(IRS_THRESH_OFFSET))] = 1800
        
    # Push this register map assignment onto the transaction list.
    # Since this dictionary is not ordered, the register assignment
    # order by the board is not guaranteed!
    board.poke(regmap, silent=True)

    # This poke, however, WILL have the board execute register assignments in the same
    # order as they were made in the Python
    # Note that you can also poke silently, and no response from the board will be returned
    board.poke(o_regmap)

    # You can also just peek and poke immediately
    board.pokenow(asic(IRS_TBBIAS_ADDR), 500)
    board.poke(asic(IRS_TBBIAS_ADDR), 250, silent=True)
    
    # Process all pending transactions
    response = board.transact()

    # Note that silent transactions appear as their serialized byte representation
    # still, since no response was received and parsed back into a register map
    for k,result in enumerate(response):
        print("Transaction %d:\n" % k, result.payload)

    # Clear the list before doing transactions again
    board.clearTransactions()

    # DISCUSSION
    # 
    # A register map is very naturally a map, so we use the natural map type (dictionary).
    # The use of lambda (anonymous) functions increases readability significantly.
    # It nearly reads like English, imo.
    #
    # Some comments on slickness:
    #    for chan in [(lambda x : ASIC_CHANNEL_JUMP * chanNum | x) for chanNum in range(0,8)]:
    #
    # Will not work.  You have to nest with an additional lambda expression because the chanNum
    # showing up inside the lambda is not evaluated until the list is finished being built,
    # at which point chainNum = 7.  This is the first stupid thing I've seen Python do....
    

if len(sys.argv) < 2:
    print("Usage: %s <broadcast address>" % sys.argv[0], file=sys.stderr)
    exit(1)

print("")
print("Less hacky IRS3D trigger setting template")
print("----------------------------------")

# Just got ahead and blast to all boards
# The current versions will just deadcode for registers they don't support
boards = lappd.discover(sys.argv[1])

for myboard in boards:

    # You probably want to filter boards...
    
    print("Connected to board: %s @ %s\n-------------------------" % (myboard.dna.hex(), myboard.dest))

    input("Press Enter to initiate register reset...")
    myboard.pokenow( IRS_REGRST_ADDR , 0x1 )
    print("...done.")

    input("Aiming at self...")
    myboard.aimNBIC()

    # Lets confirm that its stored in big endian order
    result = myboard.peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTIP)

    # If it is, this will print out the bytes reversed, since it expects
    # little endian
    print("%s" % hex(result))
    
    myboard.pokenow( 0x1000 , 0x2 )
    myboard.pokenow( 0x1004 , 0x1 )
    # # Kkeefe
    # # the register write to attempt a software trigger:
    # myboard.pokenow( 0x1028,  0x1 )
    input("Firing once...")
    myboard.pokenow( 0x1028 , 0x1 )
    input("...done.")

    print("Press Enter to initiate configuration...") 
    for asicNum in range(0,8):
        configIrsTrigger(myboard, 0)        
    print("...done.")
