# CSIE 7190 Cryptography and Network Security, Spring 2018

This is a introduction for usage of the code used to solve the CTF challenges in __[Homework2](https://ceiba.ntu.edu.tw/course/f378f5/hw/hw2.zip)__

# Content
- [Can't Beat CBC](#Can't-Beat-CBC)
	- [CBC 1](#CBC-1)
	- [CBC 2](#CBC-2)
	- [CBC 3](#CBC-3)
- [Man-in-the-middle Attack](#Man-in-the-middle-Attack)
- [Cloudburst](#Cloudburst)
- [One-time Wallet](#One-time-Wallet)
- [TLS Certificate](#TLS-Certificate)

# Can't Beat CBC

There are three sub-tasks.

### CBC 1

Run `4-1_cut.py` and insert "296e12d608ad04bd3a10b71b9eef4bb6ae1d697d1495595a5f5b98e409d7a7c437f24e69feb250b347db0877a40085a9" to cut the ciphertext into three blocks.

Input
```
python 4-1_cut.py
296e12d608ad04bd3a10b71b9eef4bb6ae1d697d1495595a5f5b98e409d7a7c437f24e69feb250b347db0877a40085a9
```
Output
```
48
296e12d608ad04bd3a10b71b9eef4bb6
ae1d697d1495595a5f5b98e409d7a7c4
37f24e69feb250b347db0877a40085a9
```

Then run `4-1_solve.py` to get the flag.

Input
```
python 4-1_solve.py
```
Output
```
[+] Opening connection to 140.112.31.96 on port 10124: Done
[*] Closed connection to 140.112.31.96 port 10124
BALSN{IV=KEY=GG}
```

### CBC 2

Run `4-2_poa.py` to perform Padding Oracle Attack.

Input
```
python 4-2_poa.py -c 30714b4c7a793530736b6e7a55354e67630a7f704723502797c9e4d112b2f2ae7232c30dc752bc451d691528b6901f372cd7a4b065f95e473b9675e321e6e901f4e091dc8403f4d25fec65b55177dc172c122a39c7d597f83c460d8f85a4c6f2 -l 16
```
Output
```
[+] Decrypted value (HEX): 42414C534E7B31545F31355F563352595F46554E5F54305F3533335F5448335F464C34475F3450503334525F304E335F42595F304E335F52314748545F58447D10101010101010101010101010101010
[+] Decrypted value (ASCII): BALSN{1T_15_V3RY_FUN_T0_533_TH3_FL4G_4PP34R_0N3_BY_0N3_R1GHT_XD}
```

# Man-in-the-middle Attack

Run `5_guess.py` to guess for the g in the Diffie Hellman key exchange. You will have to alter the guessing round by modifying the code inside. For example, to guess the password in round 1...

Input
```
python 5_guess.py
```
Output
```
[+] found g!!!!
[+] 13, 11677598211667310336555747471564768480113784666401373032651472276185766747825273797024874251667674512352735365370323944375386739200824333154659211686418935435931212935974800717117315759480277244620123867226222322907363783446163466090458191176989569483426321481942539054054027820690046031977417740552166504836
[+] 11993804452420291210750846533940564800913490085431228948297498333366635147627015456604540747684108474648021736442142056661148293654778290880915396576689276
[+] 11993804452420291210750846533940564800913490085431228948297498333366635147627015456604540747684108474648021736442142056661148293654778290880915396576689276
```

Then we know the password in round 1 is 13.

By doing this method three times, we have 13, 19, 17. Then run `5_solve.py` to solve for the flag.

Input
```
python 5_solve.py
```
Output
```
[+] Opening connection to 140.112.31.96 on port 10127: Done
[+] Receiving all data: Done (155B)
[*] Closed connection to 140.112.31.96 port 10127
BALSN{Wow_you_are_really_in_the_middle}
```

# Cloudburst

use `nmap` to find all IP with port 443 listening, put result IP into `open.txt`
```
nmap -n 140.112.0.0/16 -p 443 --open -oG - | awk '/Up$/{print $2}' >> open.txt
```
Then compare all fingerprint inside `open.txt` with `6_solve.py`

Input
```
python 6_solve.py
```
Output
```
============================================================= 
[+] Found matched fingerprint
[+] IP: 140.112.91.250
[+] SHA1: 6ee4b82b8a0f9c24a11d22c75b9a8519a5647b76 =============================================================
```

Connect to `https://140.112.91.250` with browser and get flag.

# One-time Wallet

Run `7_solve.py` to get flag.

Input
```
python 7_solve.py
```
Output
```
Balance: 100 BTC
Password: ?

You just got 100 BTC!
BALSN{R3tir3_4t_tw3nty}
```

# TLS Certificate

Generate signing request using `openssl`
```
openssl req -new -key rootCA.key -out power_ranger.csr 
```
Then sign the certificate
```
openssl x509 -req -in power_ranger.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out power_ranger.crt -days 500 -sha256
```

Then run `8_solve.py` to submit certificate to server

Input
```
python 8_solve.py
```
Output
```
[+] Opening connection to 140.112.31.96 on port 10129: Done
[+] Receiving all data: Done (52B)
[*] Closed connection to 140.112.31.96 port 10129
OK! You are one of balsn: BALSN{t1s_ChAiN_0f_7ru5t}
```