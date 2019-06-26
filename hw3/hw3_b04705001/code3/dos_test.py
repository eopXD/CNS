#!/usr/bin/env python2.7
import time

start = time.time()
print "Reading normal_input.txt ..."
file = open("normal_input.txt","r")
ht = {}
n = int(file.readline())
for i in range(n):
    x = int(file.readline())
    ht[x] = i
print "%s seconds" % (time.time() - start)

start = time.time()
print "Reading dos.txt ..."
file = open("dos.txt","r")
ht = {}
n = int(file.readline())
for i in range(n):
    x = int(file.readline())
    ht[x] = i
print "%s seconds" % (time.time() - start)

