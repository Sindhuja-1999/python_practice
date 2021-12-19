def isPalindrome(string):
	leng=len(string)
	result=[]
	for i in range(leng-1,-1,-1):
		result.append(string[i])
	reverse_string="".join(result)
		
	if reverse_string==string:
		return True
	else:
		return False
print(isPalindrome(input()))