def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	high=[]
	low=[]
    if fastest == True:
		for i in range(len(redShirtSpeeds)):
			if redShirtSpeeds[i]>=blueShirtSpeeds[i]:
				high.append(redShirtSpeeds[i])
			else:
				high.append(blueShirtSpeeds[i])
		return sum(high)
	if fastest==False:
		for i in range(len(redShirtSpeeds)):
			if redShirtSpeeds[i]<=blueShirtSpeeds[i]:
				low.append(redShirtSpeeds[i])
			else:
				low.append(blueShirtSpeeds[i])
		return sum(low)
		
