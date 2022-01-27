def nonConstructibleChange(coins):
	dup=sorted(coins)
	change=0
	
	for i in dup:
		tobecreated=change+1
		if i>tobecreated:
			return tobecreated
		change=change+i
	return change+1
		
			
		
		
		
