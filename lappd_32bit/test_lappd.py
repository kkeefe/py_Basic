#!/usr/bin/python3

import sys
import lappd
import socket
from random import randint

if len(sys.argv) < 2:
    print("Usage: %s <broadcast address>" % sys.argv[0], file=sys.stderr)
    exit(1)

print("")
print("LAPPD python interface test stub")
print("----------------------------------")

boards = lappd.discover(sys.argv[1])
for myboard in boards:
    print("Connected to board: %s @ %s\n-------------------------" % (myboard.dna.hex(), myboard.dest))

    # Try to point it to google
    myboard.aimNBIC(socket.gethostbyname("google.com"))
    
    # It should be pointing to the gateway
    maclow = myboard.peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTMAC_LOW)
    machigh = myboard.peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTMAC_HIGH)

    print("Board %s NBIC target MAC low: %s, high: %s" % (myboard.dna.hex(), hex(maclow), hex(machigh)))

print("\nOkay, now try pointing the boards at each other.  This should mac resolve individuals.")
# Multiboard shenanegains
N = len(boards)
if N > 1:

    for i in range(0,N):
        success = False
        while not success:
            try:  
                boards[i].aimNBIC(boards[(i + 1) % N].dest)
                success = True
            except Exception:
                print("Board %s failed to aim at board %s" % (boards[i].dna, boards[(i + 1) % N].dna))

    # Verify that they are pointing at each other
    for i in range(0,N):
        maclow = boards[i].peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTMAC_LOW)
        machigh = boards[i].peeknow(lappd.NBIC_OFFSET | lappd.REG_NBIC_DESTMAC_HIGH)

        print("Board %s NBIC target MAC low: %s, high: %s" % (boards[i].dna.hex(), hex(maclow), hex(machigh)))

          
       
