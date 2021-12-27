def classPhotos(redShirtHeights, blueShirtHeights):
	k=[]
	t=[]
    for i in range(len(redShirtHeights)):
		if redShirtHeights[i]>blueShirtHeights[i]:
			k.append(redShirtHeights)
		elif redShirtHeights[i]<blueShirtHeights[i]:
			t.append(blueShirtHeights[i])
		else:
			return False
			
	if len(k)==len(redShirtHeights) or len(t)==len(redShirtHeights):
		return True
	else:
		return False
