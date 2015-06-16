import sys
import dbpediaQuery
import pprint

def checkLocation(qInputVariable):
#-------------------------------------------------------
#RUNNING QUERY
#-------------------------------------------------------
	queryFile = "queries/checkLocation.rq"
	results = dbpediaQuery.query(queryFile, qInputVariable)
	
#-------------------------------------------------------
#READING JSON AND RETURNING BOOLEAN VALUE
#------------------------------------------------------- 
	return bool(results['boolean'])

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	results = checkLocation(qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
