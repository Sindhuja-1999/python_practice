def moveElementToEnd(array, toMove):
	move=[]
	rem=[]
	for i in array:
		if i==toMove:
			move.append(i)
		else:
			rem.append(i)
	return rem+move