######Python 3######
import operator

from Crypto.Cipher import AES
from binascii import unhexlify

class DoubleAES():
    def __init__(self, key0, key1):
        self.aes128_0 = AES.new(key=key0, mode=AES.MODE_ECB)
        self.aes128_1 = AES.new(key=key1, mode=AES.MODE_ECB)

    def encrypt(self, s):
        return self.aes128_1.encrypt(self.aes128_0.encrypt(s))

    def decrypt(self, data):
        return self.aes128_0.decrypt(self.aes128_1.decrypt(data))

def int2bytes(n):
    return bytes.fromhex('{0:032x}'.format(n))

ciphertext=unhexlify(b'3e3a9839eb6331aa03f76e1a908d746bfccaf7acb22265b725a9f1fc0644cdda')
aes2=DoubleAES(key0=int2bytes(6298659),key1=int2bytes(4272711))
plaintext=aes2.decrypt(ciphertext)

print(plaintext)