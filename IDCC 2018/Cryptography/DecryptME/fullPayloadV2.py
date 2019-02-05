from base64 import *

enkripsi = open('enkripsi','r').read()

integer = []
for i in range(len(enkripsi)):
	integer.append(ord(enkripsi[i]) + 127)

cekparam = b64encode('IDCC{')
kunci = []

for i in range(4):
	for j in range(0,127):
		cek = integer[i] - j
		if chr(cek) == cekparam[i]:
			kunci.append(j)

flag = ''
for i in range(len(integer)):
	tmp = integer[i] - kunci[i % len(kunci)]
	flag += chr(tmp)
print b64decode(flag)