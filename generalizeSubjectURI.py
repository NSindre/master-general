import sys
import dbpediaQuery
import pprint

def generalizeSubjectURI(qInputVariable):
#-------------------------------------------------------
#RUNNING QUERY
#-------------------------------------------------------
	queryFile = "queries/generalizeSubjectURI.rq"
	results = dbpediaQuery.query(queryFile, qInputVariable)
	
#-------------------------------------------------------
#READING JSON AND RETURNING A LIST OF URIS
#------------------------------------------------------- 
	subjectList = []
	for result in results["results"]["bindings"]:
		subjectList.append(result["gen"]["value"])
	return(subjectList)

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	results = generalizeSubjectURI(qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
