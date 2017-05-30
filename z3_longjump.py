import struct, binascii
from z3 import *

solver=Solver()

var = []
for i in range(8):
	var.append(BitVec('a%i'%i,32))
	solver.add(Or(And(var[i]&0xff >= 0x30,var[i]&0xff <= 0x39),And(var[i]&0xff >= 0x41,var[i]&0xff <= 0x46)))
	solver.add(Or(And((var[i]>>8)&0xff >= 0x30,(var[i]>>8)&0xff <= 0x39),And((var[i]>>8)&0xff >= 0x41,(var[i]>>8)&0xff <= 0x46)))
	solver.add(Or(And((var[i]>>16)&0xff >= 0x30,(var[i]>>16)&0xff <= 0x39),And((var[i]>>16)&0xff >= 0x41,(var[i]>>16)&0xff <= 0x46)))
	solver.add(Or(And((var[i]>>24)&0xff >= 0x30,(var[i]>>24)&0xff <= 0x39),And((var[i]>>24)&0xff >= 0x41,(var[i]>>24)&0xff <= 0x46)))

#			1d41	930e	   18c0	    1aab	   4beb	      02a0	   d880	  0381
solver.add(var[0] + var[1] + var[2] + var[3] + var[4] + var[5] + var[6] + var[7] == 0xbcdfd0a4)
solver.add(var[0] + var[1]*2 + var[2] + var[3]*2 + var[4] + var[5]*2 + var[6] + var[7]*2 == 0x93cca16e)
solver.add(var[0] + var[1]*2 + var[2]*2 + var[3]*2 + var[4]*2 + var[5]*2 + var[6]*2 + var[7] == 0x35b29de)
solver.add(var[0] + var[1] + var[2]*2 + var[3]*2 + var[4]*2 + var[5]*2 + var[6] + var[7] == 0x9bd3c16b)
solver.add(var[0] + var[1]*2 + var[2]*3 + var[3]*5 + var[4] + var[5]*2 + var[6]*3 + var[7]*5 == 0xe427de94)
solver.add(var[0] + var[1]*3 + var[2]*5 + var[3]*7 + var[4] + var[5]*3 + var[6]*5 + var[7]*7 == 0x228111b4)
solver.add(var[0] + var[1]*2 + var[2]*3 + var[3]*4 + var[4]*5 + var[5]*6 + var[6]*7 + var[7]*8 == 0xe774009c)
solver.add(var[0] + var[1]*4 + var[2]*6 + var[3]*8 + var[4]*2 + var[5]*3 + var[6]*5 + var[7]*7 == 0x3840179)

print solver.check()
modl = solver.model()
print modl

flag = [0,1,2,3,4,5,6,7]

for i in range(8):
	flag[int(str(modl[i])[1:])] = struct.pack("<I",modl[modl[i]].as_long())

print "".join(flag)
