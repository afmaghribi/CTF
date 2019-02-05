from base64 import *
def enkripsi(plain, keys):
	enc = []
	plain = b64encode(plain)
	for i, l in enumerate(plain):
		kunci = ord(keys[i % len(keys)]) #integer dari huruf ke .. yang hasil dari panjang plain -1 di mod panjang key
		teks = ord(l) #integer dari huruf di base64
		enc.append(chr((teks + kunci) % 127))
	return ''.join(enc)
