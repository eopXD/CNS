#!/usr/bin/python
 
import signal, sys, os, time
import random
import hashlib

import base64
import binascii

from pwn import *

# prime
p = 262603487816194488181258352326988232210376591996146252542919605878805005469693782312718749915099841408908446760404481236646436295067318626356598442952156854984209550714670817589388406059285064542905718710475775121565983586780136825600264380868770029680925618588391997934473191054590812256197806034618157751903


# generate all possible g
g = []
for i in range(1,20+1):
	tmp = int(hashlib.sha512(str(i)).hexdigest(), 16)
	tmp = pow(tmp,2,p)
	g.append(tmp)

	
i = 1
for _ in g:
	A = remote("140.112.31.96",10127)
	B = remote("140.112.31.96",10127)
	# round x
	a = A.recvuntil("Server sends: ")
	b = B.recvuntil("Server sends: ")
	x = A.readline()
	y = B.readline()
	x = int(x[:-1])
	y = int(y[:-1])
	A.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	B.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	tmp = pow(_,3,p)
	A.sendline(str(tmp))
	B.sendline(str(tmp))
	# round a
	a = A.recvuntil("Server sends: ")
	b = B.recvuntil("Server sends: ")
	a = A.readline()
	b = B.readline()
	a = a[:-1]
	b = b[:-1]
	A.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	B.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	A.sendline(b)
	B.sendline(a)
	
	# round b
	a = A.recvuntil("Server sends: ")
	b = B.recvuntil("Server sends: ")
	a = A.readline()
	b = B.readline()
	a = a[:-1]
	b = b[:-1]
	A.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	B.recvuntil("Generate 'a' and send A = g^a mod p to the server: ")
	A.sendline(b)
	B.sendline(a)
		
	# recieve FLAG
	A.recvuntil("FLAG is: ")
	B.recvuntil("FLAG is: ")
	a = A.recvall()
	b = B.recvall()
	a = a[:-1]
	b = b[:-1]
	a = int(a)
	b = int(b)

	x = pow(x,3,p)
	y = pow(y,3,p)
	a ^= int(hashlib.sha512(str(x)).hexdigest(), 16)
	b ^= int(hashlib.sha512(str(y)).hexdigest(), 16)
	if a == b:
		print "[+] found g!!!!"
		print "[+] " + str(i) + ", " + str(_)
		print "[+] " + str(a)
		print "[+] " + str(b)
		break
	i = i + 1

# g1 = 12
# g2 = 18
# g3 = 16