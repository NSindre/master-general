import sys
import os.path
from findTermData import findTermData
import pprint
try:
	import cPickle as pickle
except:
	import pickle

def getTermRecords(inputType, qInputVariable):
	outDataDirectory = "outData/"
	variableFileName = qInputVariable.lower().replace(' ','_')+".p"
	termDataList = []
	overwrite = False
#-------------------------------------------------------
#CHECKING FOR RECORD OF PREVIOUS SEARCH FOR SAME VARIABLE
#-------------------------------------------------------
	hasRecord = os.path.isfile(outDataDirectory+variableFileName)
#-------------------------------------------------------
#LOADING OLD ENTRY
#-------------------------------------------------------
	if hasRecord:
		print("Loading <"+qInputVariable+"> data from file: "+outDataDirectory+variableFileName)
		with open(outDataDirectory+variableFileName, rb) as recordFile:
			termDataList = pickle.load(recordFile)
#-------------------------------------------------------
#MAKING NEW ENTRY
#-------------------------------------------------------
	if overwrite or not hasRecord:
		print("Making new <"+qInputVariable+"> data.")
		termDataList = findTermData(inputType, qInputVariable)

		#Saving the new entry in a file
		with open(outDataDirectory+variableFileName, wb) as recordFile:
			print("Saving record to: "+outDataDirectory+variableFileName)
			pickle.dump(termDataList, recordFile)
#-------------------------------------------------------
#RETURNING LIST, EITHER LOADED FROM FILE OR JUST MADE
#-------------------------------------------------------
	return(termDataList)

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	inputType = str(sys.argv[1])
	qInputVariable = str(sys.argv[2])
	print(qInputVariable +": ")
	results = getTermRecords(inputType, qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
