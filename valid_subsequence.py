def isValidSubsequence(array, sequence):
	c=-1
	"""output = []
	for x in sequence:
		if x not in output:
			output.append(x)
	"""
	for j in sequence:		
		if j in array and array.index(j)>c:
			c=array.index(j)
		
		else:
			return False
	return True
t=int(input())
p=[]
for i in range(t):
    p.append(int(input())
h=int(input())
q=[]
for i in range(h):
    q.append(int(input())

print(isValidSubsequence(p,q))	
			