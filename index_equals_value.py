def indexEqualsValue(array):
	for i in range(len(array)):
		if i==array[i]:
			return i
		else:
			continue
	return -1