#!/usr/bin/python
 
import signal, sys, os, time
import random
import hashlib

import base64
import binascii

from pwn import *

# prime
p = 262603487816194488181258352326988232210376591996146252542919605878805005469693782312718749915099841408908446760404481236646436295067318626356598442952156854984209550714670817589388406059285064542905718710475775121565983586780136825600264380868770029680925618588391997934473191054590812256197806034618157751903

password = [13,19,17]
#print password
assert(len(password) == 3)
assert(all(0 < i <= 20 for i in password))
password = [int(hashlib.sha512(str(i)).hexdigest(), 16) for i in password]
#print password
A = remote("140.112.31.96",10127)
key = 0 
for i,pwd in enumerate(password):
	#print 'Round', i+1
	a = A.recvuntil("Server sends: ")
	a = A.readline()
	a = int(a[:-1])
	
	g = pow(pwd,2,p)
	b = 3
	B = pow(g,b,p)
	A.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	A.sendline(str(B))
	K = pow(a,b,p)
	key ^= int(hashlib.sha512(str(K)).hexdigest(), 16)

A.recvuntil("FLAG is: ")
_ = A.recvall()
_= int(_[:-1])

flag = _ ^ key


print binascii.unhexlify('%x' % flag)
# BALSN{Wow_you_are_really_in_the_middle}
