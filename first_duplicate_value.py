def firstDuplicateValue(array):
	su=0
    for i in array:
		if array.count(i)>1:
			p=sum(array.index(i))
			if p>su:
				su=su+p				
			else:
				return i		
			
			
	return -1
		
	
	
		
		
