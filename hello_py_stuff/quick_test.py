#!/usr/bin/python3

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

# # lets make a file to write and store data stuff with from a python script
# import json
# pixelData = 'pixelData.json'
# with open(pixelData) as f:
    # allPixelData = json.load(f)

# savePixelData = 'savePixelData.txt'
# with open(savePixelData , "w") as f1:
    # f1.write('{0}\t{1}\n'.format('pixelNum ', 'readNum'))
    # for pixelMap in allPixelData["allPixelMappings"]:
        # pixelNum = pixelMap['pixelNum']
        # readNum  = pixelMap['readNum']
        # print(pixelNum , readNum)
        # f1.write('{0}\t{1}\n'.format(pixelNum , readNum))

# make a class to store all of the asic attributes
class AsicSettings():
    def __init__(self):
        # asic specific stuff
        self.vbias  = 0
        self.vbias2 = 0
        self.itbias = 0
        self.tbbias = 0
        self.digreg = 0
        # channel specific stuff
        self.ChannelSettings()

class ChannelSettings():
    def __init__(self, channel=None):
        # physical location
        # set of channels
        self.wbias = 0
        self.vofs1 = 0
        self.vofs2 = 0
        self.thresh_offset = 0

class Asic():
    def __init__(self, row, col, num, AsicSettings, schan=[],):
        # physical location
        self.row = 0
        self.col = 0
        self.num = 0
        # set of channels
        self.chan = [0,1,2,3,4,5,6,7]
        self.AsicSettings()

class trigFSM():
    def __init__(self):
        self.data_addr_bef = 0
        self.data_addr_aft = 0
        self.data_addr_offset = 0
        self.data_addr_bitCount = 0
        self.soft_trig_en = bool

class PixelData():
    def __init__(self, data={}):
        self.data = data

class Pixel():
    def __init__(self, pixelNum, bitNum, asicNum, asicCh, PixelData):
        self.pixelNum = 0
        self.bitNum   = 0
        self.asicNum  = 0
        self.asicCh   = 0
        self.data     = PixelData()

# make a class to store all of the board attributes
class IrsBoard(lappd.Board):
    def __init__(self, ipAddr, name="IrsBoard", Asics=[], regMap={}):
        super().__init__(ipAddr)
        self.name = name
        self.Asics = Asics
        self.regMap = regMap
