#!/usr/bin/env python
import signal
import sys
import os
import time
import random
import string

import ssl
import socket
import hashlib

from OpenSSL import crypto 
fingerprint = "6ee4b82b8a0f9c24a11d22c75b9a8519a5647b76"
file = open("open.txt","r")

while 1:
	ip = file.readline()
	ip = ip[:-1]
	if len(ip) == 0:
		break
	#print "[+] now trying on...", ip
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.5)
	wrappedSocket = ssl.wrap_socket(sock)
	try:
		wrappedSocket.connect((ip, 443))
	except:
		response = False
	else:
		der_cert_bin = wrappedSocket.getpeercert(True)
		pem_cert = ssl.DER_cert_to_PEM_cert(wrappedSocket.getpeercert(True))
	 	cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem_cert)
		tmp_fingerprint = hashlib.sha1(der_cert_bin).hexdigest()
		#print "[+] Fingerprint: " + tmp_fingerprint
	 	if tmp_fingerprint == fingerprint:
	 		print "============================================================================="
			print "[+] Found matched fingerprint"
	 		print "[+] IP: " +  ip
	 		print "[+] SHA1: " + tmp_fingerprint
	 		print "============================================================================="
