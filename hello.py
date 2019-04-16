print("this line will be printed")

mult = lambda x,y: x * y
print(mult(2,3))

IRS_OFFSET_JUMP   = 0x0100 << 2
IRS_OFFSET_ADDR   = 0x4000
asic = lambda x,y : (IRS_OFFSET_ADDR | y * IRS_OFFSET_JUMP | x)

print(asic(1,2))