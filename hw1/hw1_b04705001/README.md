# CSIE 7190 Cryptography and Network Security, Spring 2018

This is a introduction for usage of the code used to solve the CTF challenges in __[Homework1](https://ceiba.ntu.edu.tw/course/f378f5/hw/hw1-eb852d5b1a1813776a14f83a3ab6f6d2.zip)__

# Content
- [How2Crypto](#how2crypto)
	- [Round 1](#round-1)
	- [Round 2](#round-2)
	- [Round 3](#round-3)
	- [Round 4](#round-4)
	- [Round 5](#round-5)
	- [Round 6](#round-6)

- [Mersenne RSA](#mersenne-rsa)
- [OTP](#otp)
- [Double AES](#double-aes)
- [Time Machine](#time-machine)
- [Future Oracle](#future-oracle)
- [Digital Saving Account](#digital-saving-account)


## How2Crypto

There is a total of 6 rounds.

### Round 1
Insert `c1` into program compiled by `4_1.cpp`
```
$ g++ 4_1.cpp -o 1
$ ./1
>> c1 = ????????????????????????????????
```
The direct output would be the decrypted text.

### Round 2
Insert `m1`, `c1`, and `c2` (a empty line between c1 and c2) into program compiled by `4_2.cpp`
```
$ g++ 4_2.cpp -o 2
$ ./2
>> m1 = ????????????????????????????????
>> c1 = ????????????????????????????????
>> 
>> c2 = ????????????????????????????????
```
The direct output would be the decrypted text.


### Round 3
Insert `c1` into program compiled by `4_3.cpp`
```
$ g++ 4_3.cpp -o 3
$ ./1
>> c1 = ????????????????????????????????
```
Among all possible decrypted text, pick the most reasonable one.


### Round 4
Insert `m1`, `c1`, and `c2` (a empty line between c1 and c2) into program compiled by `4_4.cpp`
```
$ g++ 4_4.cpp -o 4
$ ./2
>> m1 = ????????????????????????????????
>> c1 = ????????????????????????????????
>> 
>> c2 = ????????????????????????????????
```
The direct output would be the decrypted text.

### Round 5
Insert `m1`, `c1`, and `c2` (a empty line between c1 and c2) into program compiled by `4_5.cpp`
```
$ g++ 4_5.cpp -o 5
$ ./2
>> m1 = ????????????????????????????????
>> c1 = ????????????????????????????????
>> 
>> c2 = ????????????????????????????????
```
All possible decrypted text is in `output.txt`. Find the most reasonable one.

__There is still bug in the program, which may fail to decrypt.__

### Round 6
Insert `c1` into this [online_site](https://www.dcode.fr/rail-fence-cipher). Pick the most reasonable text decrypted.

At last, decode the flag with `4_decode_flag.py`
```
python 4_decode_flag.py
```
`flag.png` is the flag.

## Mersenne RSA

Get inverse `d` with `5_inverse.py`. Then get `m` with `5_getm.py`. At last decode the `m` with `5_decode.py` and it will print out the flag.
```
python 5_inverse.py
python 5_getm.py
python 5_decode.py
```

## OTP

Use `6_guess_length.cpp` to find reasonable key length. Then observe `output.txt` for the key value. Then use `6_decode.cpp` to get the decrypted text.
```
g++ 6_guess_length.cpp -o guess
./guess
g++ 6_decode.cpp -o decode
./decode
```
The decoded text would be the output.

## Double AES

Get key using `7_brutedorce.py`
```
python 7_bruteforce.py
```
Then use `7_decrypt.py` to get flag.
```
python 7_decrypt.py
```
The decoded text would be the output.

## Time Machine

Go to dicrectory `8`. Then
```
python collide.py
```
Flag would be in the output.

## Future Oracle

Simply run `9.py`
```
python 9.py
```

## Digital Saving Account

Run `cut_n_paste.py` to find account and password for admin mode. After logging in the the new token, insert `public key` and `transaction` into `interface.py`. 
```
ip71-170:digital_saving_account eopXD$ python interface.py
INFO:DSAregenK:---- start inserting known message and attributes ----
insert p: p = 130692160919700276455421124612997939767003434213452743312935182126058445096205092083756816974066470897223962605060796814523749304054643228280971494378855034260467619596586484897285201908625104363524968365581956238529315568303205206617406305836861586215140962348790471856437575868537228804711532939573079430037
q = 1401456235240904702777824972302024901882008037267
g = 95396451494886081219955330737787062495856026230850865981748040019965339824242689763063003743776157423703080354926214378202714467203868752083428448336602164955985281816971999717840089591556177199398205241590732285318961289456953516724125358518819601937299791992889961873422741408219630281194017450035149490141
y = 114323837905952364929612228480137791495434619992093236340531300461416520233047431704001615086092525401985379403435923866725764839204869671066666403333830086163857826205828115541538047539527263628277792424756862353613020812429158127758724410885916216051320024672454648514946034646356950659741215279396267853211insert q: insert g: insert y:
----------
<_DSAobj @0x10a6c0320 y,g,p(1024),q>
114323837905952364929612228480137791495434619992093236340531300461416520233047431704001615086092525401985379403435923866725764839204869671066666403333830086163857826205828115541538047539527263628277792424756862353613020812429158127758724410885916216051320024672454648514946034646356950659741215279396267853211
95396451494886081219955330737787062495856026230850865981748040019965339824242689763063003743776157423703080354926214378202714467203868752083428448336602164955985281816971999717840089591556177199398205241590732285318961289456953516724125358518819601937299791992889961873422741408219630281194017450035149490141
130692160919700276455421124612997939767003434213452743312935182126058445096205092083756816974066470897223962605060796814523749304054643228280971494378855034260467619596586484897285201908625104363524968365581956238529315568303205206617406305836861586215140962348790471856437575868537228804711532939573079430037
1401456235240904702777824972302024901882008037267
----------
DEBUG:DSAregenK:---- Input -- mA ----
insert m: Transaction1: 648459954059642878418385613085
sig("648459954059642878418385613085"): 400293379562160206068795485679568296304486745963 340371312006102843079691648744605689260950989437

Transaction2: 75801978187564490776903541831
sig("75801978187564490776903541831"): 400293379562160206068795485679568296304486745963 473063094894824597044913883881157560845352339041insert(r,s): DEBUG:DSAregenK:---- Input -- mB ----
insert m: insert(r,s):
DEBUG:DSAregenK:---- input complete ----
DEBUG:DSAregenK:---- attack weak coefficient k ----
DEBUG:DSAregenK:+ set: pubkey = <_DSAobj @0x10a6c0320 y,g,p(1024),q>
DEBUG:DSAregenK:[*] reconstructing PrivKey for Candidate r=400293379562160206068795485679568296304486745963
INFO:DSAregenK:privkey reconstructed: k=645132190147978882564605506629378566224604386644; x=1126609410314076732153811283929003612576836259713;
INFO:DSAregenK:Reconstructed private_key: <_DSAobj @0x10a6c03f8 y,g,p(1024),q,x,private> | x=1126609410314076732153811283929003612576836259713
DEBUG:DSAregenK:----------------------------------------------------------
DEBUG:DSAregenK:---- Verify by x ----
DEBUG:DSAregenK:Calculated y: 114323837905952364929612228480137791495434619992093236340531300461416520233047431704001615086092525401985379403435923866725764839204869671066666403333830086163857826205828115541538047539527263628277792424756862353613020812429158127758724410885916216051320024672454648514946034646356950659741215279396267853211
DEBUG:DSAregenK:Inserted y: 114323837905952364929612228480137791495434619992093236340531300461416520233047431704001615086092525401985379403435923866725764839204869671066666403333830086163857826205828115541538047539527263628277792424756862353613020812429158127758724410885916216051320024672454648514946034646356950659741215279396267853211
INFO:DSAregenK:Verified! Successfully reconstructed x!!!
DEBUG:DSAregenK:---- Verify by r ----
Insert k from output message: 645132190147978882564605506629378566224604386644
DEBUG:DSAregenK:Calculated r: 400293379562160206068795485679568296304486745963
DEBUG:DSAregenK:Inserted   r: 400293379562160206068795485679568296304486745963
INFO:DSAregenK:Verified! Successfully reconstructed r!!!
DEBUG:DSAregenK:Calculated s: 340371312006102843079691648744605689260950989437
DEBUG:DSAregenK:Inserted   s: 340371312006102843079691648744605689260950989437
INFO:DSAregenK:Verified! Successfully reconstructed s!!!
r =  400293379562160206068795485679568296304486745963
s =  752514819009360344627564539411746050036265689483
```
Then with the output, copy it back to the admin mode with `3)Get Flag`. 