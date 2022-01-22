def caesarCipherEncryptor(string, key):
	p=list(map(chr, range(97, 123)))
	lis=""
	for i in p:
		for i in string:
			q=p.index(i)
			if q+key>122:
				lis.join(p[q+key-26])
			elif q+key<=122:
				lis.join(p[q+key])
	return lis
