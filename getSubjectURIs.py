import sys
import dbpediaQuery
import pprint

def getSubjects(qInputVariable):
#-------------------------------------------------------
#PREPARING QUERY
#-------------------------------------------------------
	qTerm = qInputVariable.split()
	qTerm[0] = qTerm[0].capitalize() #if you want to capitalize input, do it here
	qTerm = ' '.join(qTerm)
	#capitalization of is done because everything in dbpedia and wibitaxonomy is capitalized
	#only the first word is changed, to make sure locations like "Playa del Carmen" remain intact
	#ignoring capitalization in a large dataset like dbpedia is extremely expensive
#-------------------------------------------------------
#RUNNING QUERY
#-------------------------------------------------------
	queryFile = "queries/getSubjectURIs.rq"
	results = dbpediaQuery.query(queryFile, qTerm)
	
#-------------------------------------------------------
#READING JSON FROM QUERY AND RETURNING A LIST OF URIS
#------------------------------------------------------- 
	subjectList = []
	for result in results["results"]["bindings"]:
		subjectList.append(result["s"]["value"])
	return(subjectList)

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	results = getSubjects(qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
