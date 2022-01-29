def runLengthEncoding(string):
	em=""
	
	lst=list(string)
	q=set(lst)
	sub=sorted(list(q))
	p=[]
	for i in range(len(sub)):
		t=lst.count(sub[i])
		if t>9:
			p.append(9)+p.append(t-9)
		else:
			
			p.append(t)
	return p	
		
		
	# c=0
	# p=None
	# for i in lst:
	# 	if p==None:
	# 		p=i
	# 	elif p==i:
	# 		c=c+1
			
		
	# for i in string:
	# 	q=len(i)
	# 	if len(i)<10:
	# 		return qi
	# 	else:
	# 		return 9i+(q-9)i
	