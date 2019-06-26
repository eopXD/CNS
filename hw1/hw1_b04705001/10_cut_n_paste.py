import signal
import sys
import os
import time

from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode

BLOCK_SIZE = 16
def get_L ( ):
	token = raw_input("Insert token1: ")
	token = token.decode("base64")
	print len(token)
	block = ""
	i = 0
	while i < len(token) :
		block = block + token[i]
		i = i + 1
		if i == BLOCK_SIZE * 2 :
			return block


def get_R ( ) :
	token = raw_input("Insert token2: ")
	token = token.decode("base64")
	print len(token)
	block = ""
	i = BLOCK_SIZE * 2

	while i < len(token) :
		block = block + token[i]
		i = i + 1
	return block

A = get_L()
B = get_R()
print b64encode(A)
print b64encode(B)

token = A + B

print b64encode(token)