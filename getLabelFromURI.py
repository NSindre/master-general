import sys
import dbpediaQuery
import pprint

def getLabel(qInputVariable):
#-------------------------------------------------------
#RUNNING QUERY
#-------------------------------------------------------
	queryFile = "queries/getLabelFromURI.rq"
	results = dbpediaQuery.query(queryFile, qInputVariable)
	
#-------------------------------------------------------
#READING JSON AND RETURNING A SINGLE LABEL
#------------------------------------------------------- 
	for result in results["results"]["bindings"]:
		return(result["label"]["value"])
#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	results = getLabel(qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
