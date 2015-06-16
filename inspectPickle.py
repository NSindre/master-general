import sys
import pprint
try:
	import cPickle as pickle
except:
	import pickle
#-------------------------------------------------------
#Reads a pickled file and returns whatever it contains
#-------------------------------------------------------
def inspectPickle(fileName):
	with open(fileName,'rb') as pFile:
		data = pickle.load(pFile)
	return data

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	fileName = str(sys.argv[1])
	results = inspectPickle(fileName)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
