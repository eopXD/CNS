import signal
import sys
import os
import time

from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode

BLOCK_SIZE = 16

first_block = "QQ Homework is t"


token = raw_input("Insert token: ")
token = token.decode("hex")
print len(token)
blocks = []

i = 0
string = ""
while i < len(token):
	string = string + token[i]
	i = i + 1
	if len(string) == BLOCK_SIZE:
		blocks.append(string)
		string = ""

for block in blocks:
	print block.encode("hex")

