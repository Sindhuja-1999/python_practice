def findThreeLargestNumbers(array):
	sortedarray=sorted(array)
	sortedarray.reverse()
	p=sortedarray[:3]
	p.reverse()
	return p
print(findThreeLargestNumbers(list(map(int,input().split()))))