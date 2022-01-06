def isMonotonic(array):
	p=sorted(array,reverse=True)
	q=sorted(array)
	if array==p or array==q or array==[] or len(array)==1:
		return True
	# elif array==[] or len(array)==1:
	# 	return True
	else:
		return False
	