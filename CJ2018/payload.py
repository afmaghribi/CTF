angka = []

for j in range(20):
	if j <= 1:
		angka.append('1')
	else:
		tmp = int(angka[j-1]) + int(angka[j-2])
		angka.append(tmp)

for i in range(20):
	print angka[i]