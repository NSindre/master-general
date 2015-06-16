from SPARQLWrapper import SPARQLWrapper, JSON
import wibiQuery
import sys
import pprint

#-------------------------------------------------------
#This function takes a URI as input and returns wibi-entries
#for broader terms
#-------------------------------------------------------
def generalizeURI(qInputVariable):
	queryFileName = "queries/wibiGenFromURI.rq"
	results = wibiQuery.query(queryFileName, qInputVariable)

	#PUTTING RESULTS IN LIST AND RETURNING IT
	genList = []
	for result in results["results"]["bindings"]:
		genList.append(result["generalization"]["value"])
	return(genList)


#-------------------------------------------------------
#GET CALL TO FIND MATCHING PAGES IN THE WIBITAXONOMY, returns a list
#-------------------------------------------------------
def getSubjectURIs(qInputVariable):
	qInputVariable = qInputVariable.split(' ')
	qInputVariable[0] = qInputVariable[0].capitalize()
	qInputVariable = '_'.join(qInputVariable)
	termPage = "http://wibitaxonomy.org/" + qInputVariable
	termCategoryPage = "http://wibitaxonomy.org/Category%3A" + qInputVariable
	termPluralCategoryPage = "http://wibitaxonomy.org/Category%3A" + qInputVariable + "s"


	queryFileName = "queries/wibiCheckSubjectURI.rq"
	uriList = []
	if wibiQuery.query(queryFileName, termPage)['boolean']: uriList.append(termPage)
	if wibiQuery.query(queryFileName, termCategoryPage)['boolean']: uriList.append(termCategoryPage)
	if wibiQuery.query(queryFileName, termPluralCategoryPage)['boolean']: uriList.append(termPage)

	return uriList

#-------------------------------------------------------
#TURNING GENERALIZATION URIS INTO GENERALIZATIONS
#-------------------------------------------------------
def stripURI(uri):
	lastPartOfURI = (uri.rpartition('/')[2].replace('_',' '))
	return lastPartOfURI.replace('Category%3A','')
#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	subjectURIs = getSubjectURIs(qInputVariable)
	resultsList = []
	for subjectURI in subjectURIs:
		resultsList.append(generalizeURI(subjectURI))
	nameList = []
	for results in resultsList:
		for result in results:
			nameList.append(stripURI(result))
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(subjectURIs)
	pp.pprint(nameList)
