#!/usr/bin/python 2
#coding:utf-8

import signal
import sys
import os
import time
import base64
import binascii

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from pwn import *
from hashpumpy import hashpump

def sha256(content):
    Sha256 = SHA256.new()
    Sha256.update(content)
    return Sha256.digest()

def sha_it_up ( text ):
	return base64.b64encode(sha256(text))


ID = "admin"
N = "a"
flag = open("flag.txt","w")

def gogo_power_ranger ( key_length, A, B ) :

	A.sendline(ID + '||' + N + '||' + sha_it_up(ID + '||' + N))
	A.recvuntil("You should send your ID and a random string to me: ")
	Ns, trash = A.recvline().split('||')

	B.sendline(ID + '||' + Ns + '||' + sha_it_up(ID + '||' + Ns))
	B.recvuntil('You should send your ID and a random string to me: ')
	trash, mac = B.recvline().split('||')

	mac = mac.decode('base64').encode('hex')
	(h, s) = hashpump(h, ID + '||' + Ns + '||login', '||printflag', i)

	h = base64.b64encode(h.decode('hex'))
	A.sendline(base64.b64encode(s) + '||' + h)
	print(base64.b64encode(s) + '||' + h)
	power_ranger = A.recvline()
	power_ranger = A.recvline()
	if 'Integrity error' not in power_ranger:
		flag.write(A.recvall())

for i in range(15,30) :
	A = remote('140.112.31.96',10122)
	B = remote('140.112.31.96',10122)
	gogo_power_ranger(i)
	A.close()
	B.close()