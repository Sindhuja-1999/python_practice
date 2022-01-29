def runLengthEncoding(string):
	em=""
	
	lst=list(string)
	q=set(lst)
	sub=sorted(list(q))
	p=[]
	for i in range(len(sub)):
		t=lst.count(sub[i])
		if t>9:
			p.append(9)
			p.append(sub[i])
			p.append(t-9)
			p.append(sub[i])
		else:			
			p.append(t)
			p.append(sub[i])
	a=list(map(str,p))		
	return em.join(a)	
		
	