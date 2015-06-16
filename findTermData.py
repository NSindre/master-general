import sys
from generalizeSubjectURI import generalizeSubjectURI
from getSubjectURIs import getSubjects
from getLabelFromURI import getLabel
from lemmatizeGeneralTerm import lemmatize
from getFrequency import getFrequency
from checkLocation import checkLocation
from getWikipediaPage import getWikipediaPage
from dataBlock import dataBlock
import wibiGeneralizer
import pprint

def findTermData(inputType, qInputVariable):
#-------------------------------------------------------
#CONTAINERS
#-------------------------------------------------------
	termDataList = []
	subjectURIs = []
#-------------------------------------------------------
#RUNNING PIPELINE: CREATING A LIST OF DATA BLOCKS
#-------------------------------------------------------
	subjectURIs.extend(getSubjects(qInputVariable)) 			#find matching pages in dbpedia
	subjectURIs.extend(wibiGeneralizer.getSubjectURIs(qInputVariable))	#find matching pages in wibitaxonomy
	for subURI in subjectURIs:
#		wikipediaEntry = getWikipediaPage(subURI)
		if not 'wibitaxonomy' in subURI:
			wibi = False	#used to avoid redoing this check
			generalizedURIs = generalizeSubjectURI(subURI)		#find uris of generalizations in dbpedia
		else: 
			wibi = True
			generalizedURIs = wibiGeneralizer.generalizeURI(subURI)	#find uris of generalizations in wibitaxonomy
		for genURI in generalizedURIs:
			termData = dataBlock(inputType, qInputVariable)
#			termData['subjectWikiPage'] = wikipediaEntry
			termData['subjectURI'] = subURI
			termData['generalizedURI'] = genURI

			#Wibi does not use rdfs:label, so instead the final part of the URI is used
			termData['generalizedLabel'] = getLabel(genURI) if not wibi else wibiGeneralizer.stripURI(genURI)
			
			#We do not want to lemmatize generalizations that are locations
			# the check is incompatible with wibitaxonomy
			if not wibi and checkLocation(termData['generalizedURI']):
				termData['generalizedLemma'] = termData['generalizedLabel']
			else:
				try:
					termData['generalizedLemma'] = lemmatize(termData['generalizedLabel'])
				except:
					termData['generalizedLemma'] = termData['generalizedLabel']
 
			termData['generalizedFreq'] = getFrequency(termData['generalizedLemma'])
			termDataList.append(termData)
#-------------------------------------------------------
#SORTING BY FREQUENCY OF OCCURENCE
#-------------------------------------------------------
	termDataList = sorted(termDataList, key=lambda k: k['generalizedFreq'], reverse=True)
#-------------------------------------------------------
#RETURNING
#-------------------------------------------------------
	return(termDataList)
#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	inputType = str(sys.argv[1])
	qInputVariable = str(sys.argv[2])
	print(qInputVariable +": ")
	results = findTermData(inputType, qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
