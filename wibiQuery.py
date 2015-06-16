from SPARQLWrapper import SPARQLWrapper, JSON
import sys
import pprint
import codecs

#-------------------------------------------------------
#This function takes a file with a query and a variable
#It inserts the variable into the query and runs it against
#the selected endpoint.
#It then returns the results in JSON format
#-------------------------------------------------------
def query(queryFileName, qInputVariable):
#-------------------------------------------------------
#SELECTING ENDPOINT
#-------------------------------------------------------
	sparql = SPARQLWrapper("http://localhost:3030/ds/query")				#local jena-fuseki server
#-------------------------------------------------------
#PREPARING QUERY
#-------------------------------------------------------
	qString=""
	with codecs.open(queryFileName,'r','utf-8') as qFile:
		qString=qFile.read()
		qFile.close()

	qString =qString.format(qInputVariable) #this inserts the variable part into the query

	sparql.setQuery(qString)
	sparql.setReturnFormat(JSON)
#-------------------------------------------------------
#RUNNING QUERY
#-------------------------------------------------------
	results = sparql.queryAndConvert()
#-------------------------------------------------------
#RETURNING RESULTS AS JSON STRING
#-------------------------------------------------------
	return(results)
#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qFileName = str(sys.argv[1])
	qInputVariable = str(sys.argv[2])
	print(qInputVariable +": ")
	results = query(qFileName,qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
