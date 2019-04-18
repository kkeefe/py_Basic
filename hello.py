import numpy as np

# print("first lambda, mult")
# mult = lambda x,y: x * y
# print(mult(2,3))

IRS_OFFSET_JUMP   = 0x0100 << 2 # same thing as multiply by four..
IRS_OFFSET_ADDR   = 0x4000

asic = lambda x,y : (IRS_OFFSET_ADDR | y * IRS_OFFSET_JUMP | x)

# print("next, or the values....")
# print(hex(IRS_OFFSET_JUMP))

asic_dac = lambda x: bin(( IRS_OFFSET_ADDR | x << 2))
asic_dac_dic = {asic_dac(x): 0x0 for x in range(0,64)}

for count, x in enumerate(range(0,64)):
    print(count,asic_dac(x))
# print(asic_dac_dic)

print("next lambda, asic..")
print(hex(asic(1,2)))