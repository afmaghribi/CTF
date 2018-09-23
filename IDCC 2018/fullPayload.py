from base64 import *

ckflag = b64encode('IDCC{')
cipher = open('enkripsi','r').read()

intcipher = []
for i in range(len(cipher)):
	tmp = ord(cipher[i])  + 127
	intcipher.append(tmp)

key = []
for j in range(len(ckflag)-4):
	for i in range(0,127):
		cek = intcipher[j] - i
		if cek == ord(ckflag[j]):
			key.append(i)

flag = []
for i in range(len(intcipher)):
		tmp = intcipher[i] - key[i % len(key)]
		flag.append(chr(tmp))
hampirflag = ''.join(flag)
print b64decode(hampirflag)