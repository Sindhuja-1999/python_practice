def generateDocument(characters, document):
	doc=list(document)
	listchar=list(characters)	
	for i in doc:
		if i in listchar and listchar.count(i)>=doc.count(i):
			continue
		else:
			return False
	return True