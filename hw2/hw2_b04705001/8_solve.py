#!/usr/bin/env python
import signal
import sys
import os
import time
import random
import string
import base64

from pwn import *

with open("power_ranger.crt", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

A = remote("140.112.31.96",10129)
A.recvuntil("Please give me the certificate encoded in base64 format:")
A.sendline(encoded_string)

flag = A.recvall()
print flag

# BALSN{t1s_ChAiN_0f_7ru5t}