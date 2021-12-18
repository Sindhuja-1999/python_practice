def sortedSquaredArray(array):
	newArr=[]
	for i in array:
		newArr.append(i*i)		
	result=sorted(newArr)
	return result
print(sortedSquaredArray(list(map(int,input().split()))))