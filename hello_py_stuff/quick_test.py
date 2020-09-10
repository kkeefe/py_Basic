<<<<<<< HEAD
#!/usr/local/bin/python3

# silly file to quickly test quick runs of things I make like lambdas or
# small functions that i don't necessarily want to push everywhere..

# header_count  = 0
# footer_count  = 0
# frame_count   = 0
# # # use a contents manager - passes off the resource handling..
# with open('blah2.hex','r') as f:
    # # store all of the contents of the file somewhere you want.
    # file_contents = f.read()
# # separate the contents of each item into a list by line (each element is on a new line)
# words = file_contents.split('\n')
# # how many lines is the data?
# word_count = len(words)
# # words is a list, enumerate is a function which expands the list into
# # the number of the element we're on: count and the item we're looking at: valu
# for count, val in enumerate(words):
    # # do some if statements to figure out what the value is
    # if val == "daa80085":
        # # identify the header word
        # header_count += 1
    # elif val == "abaaedee":
        # # identify the footer word
        # footer_count += 1
    # elif val == '':
        # # make sure that the element we're looking at is something useful,
        # # really this just ignores blank lines, like the last line of a file..
        # print("blank and line: %s !" % count)
    # else:
        # # the data we're shipping off is split into two lines, so we want to make sure
        # # we know what half we're looking at
        # frame_count += 0.5
        # for nible in val:
            # # the data that is read from the file is read as a string but we want that to be binary..
            # # val is a string type, and this for loop looks at each letter
            # # a single letter represents four bits, which is called a 'nible'
            # hex_str  = "0x" + nible       # make the format look good, and strings support addition..
            # int_conv = int(hex_str , 16)
            # bin_rep  = bin(int_conv)

# # # print overall info, header and footer counts should match, and the frame_count should be 8.5 times longer than each
# print("header count: %s | footer count: % s | frame_count: %s "
      # % (header_count , footer_count , frame_count))
# Ex 16-6 add gdp to this bad boi!

# lets make a file to write and store data stuff with from a python script
import json

# make the pixel maps from the combined json files..
fastPixelMap = "fast_pixelData.json"
fastMap = {}
with open(fastPixelMap, "r") as f:
    allmap = json.load(f)
    fastMap = allmap['allPixelMappings']

slowPixelMap = "slow_pixelData.json"
slowMap = {}
with open(slowPixelMap, "r") as f:
    allmap = json.load(f)
    slowMap = allmap['allPixelMappings']

allPixelMappings = {}
allPixelMappings['slowoutputCard'] = slowMap
allPixelMappings['fastoutputCard'] = fastMap

allPixelMappingName = "allPixelMapping2.json"
with open(allPixelMappingName, "w+") as f:
    json.dump(allPixelMappings, f, indent=2)

# savePixelData = 'savePixelData.txt'
# with open(savePixelData , "w") as f1:
#     f1.write('{0}\t{1}\n'.format('pixelNum ', 'readNum'))
#     for pixelMap in allPixelData["allPixelMappings"]:
#         pixelNum = pixelMap['pixelNum']
#         readNum  = pixelMap['readNum']
#         print(pixelNum , readNum)
#         f1.write('{0}\t{1}\n'.format(pixelNum , readNum))

class ChannelSettings():
    def __init__(self,asicNum, chNum,wbias,vofs1,vofs2,thresh_offset):
        # physical location
        # set of channels
        asic = lambda x : (IRS_OFFSET_ADDR | asicNum * IRS_OFFSET_JUMP | x )
        chan = lambda x : (IRS_CHANNEL_JUMP * chNum | x)

        self.wbias         = asic(chan(IRS_WBIAS_OFFSET))  , wbias
        self.vofs1         = asic(chan(IRS_VOFS1_OFFSET))  , vofs1
        self.vofs2         = asic(chan(IRS_VOFS2_OFFSET))  , vofs2
        self.thresh_offset = asic(chan(IRS_THRESH_OFFSET)) , thresh_offset

class Asic():
    def __init__(self, asicNum, vbias , vbias2 , itbias , tbbias , digreg):
        # physical location
        asic = lambda x : (IRS_OFFSET_ADDR | asicNum * IRS_OFFSET_JUMP | x )

        # asic values
        self.asicNum = asicNum
        self.vbias   = asic(IRS_VBIAS_ADDR)  , vbias
        self.vbias2  = asic(IRS_VBIAS2_ADDR) , vbias2
        self.itbias  = asic(IRS_ITBIAS_ADDR) , itbias
        self.tbbias  = asic(IRS_TBBIAS_ADDR) , tbbias
        self.digreg  = asic(IRS_DIGREG_ADDR) , digreg
        # set of channels
        self.chan = []
        for i in range(0,8):
            self.chan[i] = ChannelSettings(asicNum=asicNum, chNum=i,wbias=1000,vofs1=2048,vofs2=2048,thresh_offset=2450)

# trig FSM values
class trigFSM():
    def __init__(self , num_bef , num_aft , num_offset , num_bitcount):
        self.data_addr_bef      = IRS_DATA_BEF      , num_bef
        self.data_addr_aft      = IRS_DATA_AFT      , num_aft
        self.data_addr_offset   = IRS_DATA_OFFSET   , num_offset
        self.data_addr_bitCount = IRS_DATA_BITCOUNT , num_bitcount
        self.soft_trig          = IRS_SOFT_TRIG     , 0x50f7

class PixelData():
    def __init__(self, data):
        self.data = data

# class Pixel():

#     # static variable - every pixel reads from the same address..
#     integration_time = IRS_SCALER_PRD , 0

#     def __init__(self, pixelNum, mapping):
#         for item in mapping:
#             if item['pixelNum'] == pixelNum:  # found the pixel we're looking for
#                 self.bitNum   = item['bitNum']
#                 self.asicNum  = item['jNum']
#                 self.asicCh   = item['asicChNum']
#                 self.asicRow  = item['row']
#                 self.asicCol  = item['col']
#                 self.readNum  = item['readNum']
#                 break # we found it, so we can stop looking
#         # include a place to store data for a particular pixel
#         get_scaler = lambda x: (IRS_SCALER_VAL | x << 2)
#         self.scalerVal = get_scaler(self.bitNum) , 0
#         # self.data = PixelData()

# # make a class to store all of the board attributes
# class IrsBoard(Board):
#     # only need an ip addr to find a board..
#     def __init__(self, ipAddr, name="IrsBoard@"+str(ipAddr), outputcard='slow'):
#         # make the board from the lappd.board class..
#         super().__init__(ipAddr)

#         # give each board a unique name
#         self.name = name

#         # make sure you know what kind of card you're connected to..
#         self.outputcard = outputcard # ('fast' or 'slow') card is connected to the board

#         # load the fsm members
#         self.trigFSM = trigFSM(num_bef=1 , num_aft=1 , num_offset=1 , num_bitcount=1)

#         # set the values in the transaction list
#         self.poke( self.data_addr_bef[0]      , self.data_addr_bef[1]      , silent=True )
#         self.poke( self.data_addr_aft[0]      , self.data_addr_aft[1]      , silent=True )
#         self.poke( self.data_addr_offset[0]   , self.data_addr_offset[1]   , silent=True )
#         self.poke( self.data_addr_bitCount[0] , self.data_addr_bitCount[1] , silent=True )

#         # send the info to the board and set up the fsm
#         self.transact()
#         self.clearTransactions() # useful to reduce full frame size.

#         # values to determine asic settings..
#         self.asics = []
#         for i in range(0,8):
#             self.asics[i] = Asic(asicNum=i, vbias=1100, vbias2=950, itbias=1300, tbbias=1300, digreg=5)
#             self.poke( self.asic[i].vbias[0] ,self.asic[i].vbias[1]  , silent=True )
#             self.poke( self.asic[i].vbias2[0],self.asic[i].vbias2[1] , silent=True )
#             self.poke( self.asic[i].itbias[0],self.asic[i].itbias[1] , silent=True )
#             self.poke( self.asic[i].tbbias[0],self.asic[i].tbbias[1] , silent=True )
#             self.poke( self.asic[i].digreg[0],self.asic[i].digreg[1] , silent=True )
#             # list of channels
#             self.asic[i].chan = []
#             for j in range(0,8):
#                 self.asic[i].chan[j] = ChannelSettings(asicNum=asicNum, chNum=i,wbias=1000,vofs1=2048,vofs2=2048,thresh_offset=2450)
#                 self.poke( self.asic[i].chan[j].wbias[0]         , self.asic[i].chan[j].wbias[1], silent=True )
#                 self.poke( self.asic[i].chan[j].vofs1[0]         , self.asic[i].chan[j].vofs1[1], silent=True )
#                 self.poke( self.asic[i].chan[j].vofs2[0]         , self.asic[i].chan[j].vofs2[1], silent=True )
#                 self.poke( self.asic[i].chan[j].thresh_offset[0] , self.asic[i].chan[j].thresh_offset[1], silent=True )

#             # can't read from the asic registers..
#             self.peek( IRS_ITCHY_SCRATCHY )
#             self.transact()
#             self.clearTransactions() # useful to reduce full frame size.

#         # set up an integration time for the pixels
#         # values to determine pixel mapping, thresholds, scaler counts, etc
#         self.pixels = []
#         self.mappingfile = 'all_pixel_mapping.json'
#         with open(self.mappingfile, "r") as f:
#             allmappings = json.load(f)
#             # make the check only once to see which mapping to use
#             if self.outputcard == 'slow':
#                 mapping = allmappings['slowoutputCard']
#             elif self.outputcard == 'fast':
#                 mapping = allmappings['fastoutputCard']
#             else:
#                 print("what are you doin?")
#                 return 0
#         for pixelNum in range(1,65):
#             self.pixels = Pixel(pixelNum , mapping)

filename = "blah"
filename = filename + ".txt"
print(filename)

list2 = []
for i in range(1,65):
    list2.append(i)

for count, val in enumerate(list2):
    print(count, val, list2[count])
=======
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
>>>>>>> ef1fa5f03d0dc522c35426b67da3caeb06e5339c
