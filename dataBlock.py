def dataBlock(inputType, qInputVariable):	
	data = dict(
		term = qInputVariable,
		inputType = inputType,
		subjectURI = "",
#		subjectWikiPage = "",
		generalizedURI = "",
		generalizedLabel = "",
		generalizedLemma = "",
		generalizedFreq = 0
		)
	return data
