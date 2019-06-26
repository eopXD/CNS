######Python 3######
import operator

from Crypto.Cipher import AES
from binascii import unhexlify

class DoubleAES():
	def __init__(self, key0, key1):
		self.aes128_0 = AES.new(key=key0, mode=AES.MODE_ECB)
		self.aes128_1 = AES.new(key=key1, mode=AES.MODE_ECB)

	def encrypt(self, s):
#		return self.aes128_0.encrypt(self.aes128_0.encrypt(s))
		return self.aes128_0.encrypt(s)

	def decrypt(self, data):
#		return self.aes128_1.decrypt(self.aes128_1.decrypt(data))
		return self.aes128_1.decrypt(data)


def int2bytes(n):
	return bytes.fromhex('{0:032x}'.format(n))

class KeyInTheMiddle():
	def __init__(self,c,k):
		self.ciphertext=c
		self.key=k

def binary_search(cipher, array, lo, hi):

	if hi < lo: return -1       # no more numbers
	mid = (lo + hi) // 2        # midpoint in array
	if cipher == array[mid].ciphertext:
		return mid                  # number found here
	elif cipher < array[mid].ciphertext:
		return binary_search(cipher, array, lo, mid - 1)     # try left of here
	else:
		return binary_search(cipher, array, mid + 1, hi)     # try above here

def my_search(some_string, array):     # convenience interface to binary_search()
	return binary_search(some_string, array, 0, len(array) - 1)

def test_search():
	test_qqq="ea826f89db4bb8016394c73eb24f141b"
	pos=my_search(test_qqq,key_space)
	if pos>=0 :
		print("Found at position",pos,"with key0=",key_space[pos].key)
	else :
		print("Not found...QQ")	

def beep():
    print("\a")


plaintext = 'NoOneUses2AES_QQ'
ciphertext= unhexlify(b'0e46d393fdfae760f9d4c7837f47ce51')

key_space=[]
for i in range(0,2**23):
	tmp=DoubleAES(key0=int2bytes(i),key1=int2bytes(0))
	cipher_tmp=tmp.encrypt(plaintext).hex()
	key_space.append(KeyInTheMiddle(cipher_tmp,i))
key_space.sort(key=operator.attrgetter('ciphertext'))



#for i in key_space:
#	cc=tmp.encrypt(i.ciphertext).hex()
#	print(i.ciphertext)
#	file.write(i.ciphertext)
#	file.write(' ')
#	file.write(str(i.key))
#	file.write('\n')
#file.close()

print('Key generation done....')
beep()
print('\nStart comparing ')

#test_search()
#file=open('key_encryt.txt','w')

for i in range(0,2**23):
	tmp=DoubleAES(key0=int2bytes(0),key1=int2bytes(i))
	cipher_tmp=tmp.decrypt(ciphertext).hex()
	pos=my_search(cipher_tmp,key_space)
	if pos>=0 :
		print("Found at position ",pos,"with key0=",key_space[pos].key,", with key1=",i)
#	else :
#		print(cipher_tmp,"is not in key_space")
#		file.write(cipher_tmp)
#		file.write(" is not in key_space\n")

#file.close()

beep()







