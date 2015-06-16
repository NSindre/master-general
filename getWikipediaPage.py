import sys
import dbpediaQuery
import pprint

def getWikipediaPage(qInputVariable):
#-------------------------------------------------------
#RUNNING QUERY
#-------------------------------------------------------
	queryFile = "queries/getWikipediaPage.rq"
	results = dbpediaQuery.query(queryFile, qInputVariable)
#-------------------------------------------------------
#READING JSON AND RETURNING WIKIPEDIA URL
#------------------------------------------------------- 
	for result in results["results"]["bindings"]:
 		return(result["wikiURL"]["value"])
#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	results = getWikipediaPage(qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
