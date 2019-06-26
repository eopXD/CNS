#! /usr/bin/python

'''
    Padding Oracle Attack implementation of this article https://not.burntout.org/blog/Padding_Oracle_Attack/
    Check the readme for a full cryptographic explanation
    Author: mpgn <martial.puygrenier@gmail.com>
    Date: 2016

    86b9da4af794ad79db33a0af0951a45546f96be212288eee19eb1266cb8633fb1d2c14b5ee5178ade4ab350d6b86c245b6858968888c701bef64fa9394fa7458847beb496514e91683b39bc77ed1bca0
'''

import argparse
import httplib, urllib
import re
import binascii
import sys
import time
from binascii import unhexlify, hexlify
from itertools import cycle, izip
from pwn import *

####################################
# CUSTOM YOUR RESPONSE ORACLE HERE #
####################################
''' the function you want change to adapte the result to your problem '''
#def test_validity(response,error):

# return 1 if valid/success
def test_validity (  ciphertext , remote ):
    
    remote.sendline(ciphertext)
    result = remote.recvline()
    result = result[:-1]
#    print result
    if result == "Success":
        return 1
    else:
        return 0

################################
# CUSTOM YOUR ORACLE HTTP HERE #
################################
def call_oracle(host,cookie,url,post,method,up_cipher):
    if post:
        params = urllib.urlencode({post})
    else:
        params = urllib.urlencode({})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain", 'Cookie': cookie}
    conn = httplib.HTTPConnection(host)
    conn.request(method, url + up_cipher, params, headers)
    response = conn.getresponse()
    return conn, response

# the exploit don't need to touch this part
# split the cipher in len of size_block
def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

''' create custom block for the byte we search'''
def block_search_byte(size_block, i, pos, l):
    hex_char = hex(pos).split('0x')[1]
    return "00"*(size_block-(i+1)) + ("0" if len(hex_char)%2 != 0 else '') + hex_char + ''.join(l)    

''' create custom block for the padding'''
def block_padding(size_block, i):
    l = []
    for t in range(0,i+1):
        l.append(("0" if len(hex(i+1).split('0x')[1])%2 != 0 else '') + (hex(i+1).split('0x')[1]))
    return "00"*(size_block-(i+1)) + ''.join(l)

def hex_xor(s1,s2):
    return hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1), cycle(unhexlify(s2)))))

#def run(cipher,size_block,host,url,cookie,method,post,error):
def run ( cipher, size_block ):
    cipher       = cipher.upper()
    found        = False
    valide_value = []
    result       = []
    len_block    = size_block*2
    cipher_block = split_len(cipher, len_block)

    if len(cipher_block) == 1:
        print "[-] Abort there is only one block"
        sys.exit()  
    #for each cipher_block
    for block in reversed(range(1,len(cipher_block))):
        A = remote("140.112.31.96",10125)
        A.sendline("1")
        A.recvuntil("Encrypted_FLAG:")
        A.recvline()
        A.recvline()
        A.recvline()
        A.recvline()
        A.recvline()
        if len(cipher_block[block]) != len_block:
            print "[-] Abort length block doesn't match the size_block"
            break
        print "[+] Search value block : ", block, "\n"
            
        #for each byte of the block
        for i in range(0,size_block):
            # test each byte max 255
            for ct_pos in range(0,256):
                # 1 xor 1 = 0 or valide padding need to be checked
                if ct_pos != i+1 or (len(valide_value) > 0  and int(valide_value[-1],16) == ct_pos):

                    bk = block_search_byte(size_block, i, ct_pos, valide_value) 
                    bp = cipher_block[block-1]
                    bc = block_padding(size_block, i) 

                    tmp = hex_xor(bk,bp)
                    cb  = hex_xor(tmp,bc).upper()

                    up_cipher  = cb + cipher_block[block]
                    #time.sleep(0.5)

                    # we call the oracle, our god
                    #connection, response = call_oracle(host,cookie,url,post,method,up_cipher)

                    if args.verbose == True:
                        exe = re.findall('..',cb)
                        discover = ('').join(exe[size_block-i:size_block])
                        current =  ('').join(exe[size_block-i-1:size_block-i])
                        find_me =  ('').join(exe[:-i-1])

                        sys.stdout.write("\r[+] Test [Byte %03i/256 - Block %d ]: \033[31m%s\033[33m%s\033[36m%s\033[0m\n" % (ct_pos, block, find_me, current, discover))
                        sys.stdout.flush()

                    if test_validity(up_cipher,A):

                        found = True
                        #connection.close()
                        
                        # data analyse and insert in rigth order
                        value = re.findall('..',bk)
                        valide_value.insert(0,value[size_block-(i+1)])

                        if args.verbose == True:
                            print ''
#                            print "[+] HTTP ", response.status, response.reason
                            print "[+] Block M_Byte : %s"% bk
                            print "[+] Block C_{i-1}: %s"% bp
                            print "[+] Block Padding: %s"% bc
                            print ''

                        bytes_found = ''.join(valide_value)
                        if i == 0 and bytes_found.decode("hex") > hex(size_block) and block == len(cipher_block)-1:
                            print "[-] Error decryption failed the padding is > "+str(size_block)
                            sys.exit()

                        print '\033[36m' + '\033[1m' + "[+]" + '\033[0m' + " Found", i+1,  "bytes :", bytes_found
                        print ''

                        break 
            if found == False:
                # lets say padding is 01 for the last byte of the last block (the padding block)
                if len(cipher_block)-1 == block and i == 0:
                    value = re.findall('..',bk)
                    valide_value.insert(0,"01")
                    if args.verbose == True:
                        print ''
                        print '[-] No padding found, but maybe the padding is length 01 :)'
                        print "[+] Block M_Byte : %s"% bk
                        print "[+] Block C_{i-1}: %s"% bp
                        print "[+] Block Padding: %s"% bc
                        print ''
                        bytes_found = ''.join(valide_value)
                else:
                    print "\n[-] Error decryption failed"
                    result.insert(0, ''.join(valide_value))
                    hex_r = ''.join(result)
                    print "[+] Partial Decrypted value (HEX):", hex_r.upper()
                    padding = int(hex_r[len(hex_r)-2:len(hex_r)],16)
                    print "[+] Partial Decrypted value (ASCII):", hex_r[0:-(padding*2)].decode("hex")
                    sys.exit()
            found = False

        result.insert(0, ''.join(valide_value))
        valide_value = []
        A.close()
    print ''
    hex_r = ''.join(result)
    print "[+] Decrypted value (HEX):", hex_r.upper()
    padding = int(hex_r[len(hex_r)-2:len(hex_r)],16)
    print "[+] Decrypted value (ASCII):", hex_r[0:-(padding*2)].decode("hex")

if __name__ == '__main__':                           

    parser = argparse.ArgumentParser(description='Exploit of Padding Oracle Attack')
    parser.add_argument('-c', "--cipher",               required=True,              help='cipher you want to decrypt')
    parser.add_argument('-l', '--length_block_cipher',  required=True, type=int,    help='lenght of a block cipher: 8,16')
#    parser.add_argument("--host",                       required=True,              help='url example: /page=')
#    parser.add_argument('-u', "--urltarget",            required=True,              help='url example: /page=')
#    parser.add_argument('--error',                      required=True,              help='Error that oracle give us example: 404,500,200 OR in the dom example: "<h2>Padding Error<h2>"')
#    parser.add_argument('--cookie',         help='Cookie example: PHPSESSID=9nnvje7p90b507shfmb94d7',   default="")
#    parser.add_argument('--method',         help='Type methode like POST GET default GET',              default="GET")
#    parser.add_argument('--post',           help="POST data example: 'user':'value', 'pass':'value'",    default="")
    parser.add_argument('-v', "--verbose",  help='debug mode, you need a large screen', action="store_true")
    args = parser.parse_args()
#    run(args.cipher, args.length_block_cipher, args.host, args.urltarget, args.cookie, args.method, args.post, args.error)
    run(args.cipher, args.length_block_cipher)


'''
time python cbc2_poa.py -c 30714b4c7a793530736b6e7a55354e67630a7f704723502797c9e4d112b2f2ae7232c30dc752bc451d691528b6901f372cd7a4b065f95e473b9675e321e6e901f4e091dc8403f4d25fec65b55177dc172c122a39c7d597f83c460d8f85a4c6f2 -l 16
[+] Decrypted value (HEX): 42414C534E7B31545F31355F563352595F46554E5F54305F3533335F5448335F464C34475F3450503334525F304E335F42595F304E335F52314748545F58447D10101010101010101010101010101010
[+] Decrypted value (ASCII): BALSN{1T_15_V3RY_FUN_T0_533_TH3_FL4G_4PP34R_0N3_BY_0N3_R1GHT_XD}

real    1m30.078s
user    0m6.105s
sys 0m1.041s
'''
