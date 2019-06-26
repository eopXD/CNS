import signal
import sys
import os
import time
import binascii

from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode

from pwn import *

BLOCK_SIZE = 16

def string_to_int ( string ) :
	res = ""
	for c in string:
		res = res + "{0:08b}".format(ord(c))
	return int(res,2)

m0 = "QQ Homework is t"
m1 = "oo hard, how2dec"
m2 = "rypt QQ"

e0 = "296e12d608ad04bd3a10b71b9eef4bb6"
e1 = "ae1d697d1495595a5f5b98e409d7a7c4"
e2 = "37f24e69feb250b347db0877a40085a9"

A = remote("140.112.31.96",10124)

A.sendline("1")
A.recvuntil("Ciphertext: ")
A.sendline(e1+e2)

eopXD = A.recvline()
eopXD = eopXD[:-1]
A.close()

power_ranger = ""
q = ""
i = 0 
while i < len(eopXD):
	if i < 16:
		power_ranger = power_ranger + eopXD[i]
	else:
		q = q + eopXD[i]
	i = i + 1

assert(q == "rypt QQ")

D_e1 = string_to_int(m1) ^ string_to_int(e0.decode("hex"))
IV = string_to_int(power_ranger) ^ D_e1

print binascii.unhexlify('%x' % IV)

# BALSN{IV=KEY=GG}