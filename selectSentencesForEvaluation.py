import sys
import pprint
import glob
import codecs
from inspectPickle import inspectPickle

#-------------------------------------------------------
#Computer magic, generalizium leviosa!
#-------------------------------------------------------
def getData():
	inputDir = "outData/replSentences/"
	completeDataSet = []
	for filename in glob.glob(inputDir+'*.rpls'):
		completeDataSet.append(inspectPickle(filename))
	return completeDataSet

#-------------------------------------------------------
#Who in their right mind would write bullshit comments like this
#-------------------------------------------------------	
def selectAllSentences():
	data = getData() #this is a list of lists of dictionaries
	csv_outData = "TYPE,ENTITY,SENTENCE\n"
	
	for entries in data:
		for entry in entries: #entry is a dictionary
			for sentence in entry['sentences']:	#each entry has a list of sentences
				#each sentence is a list of (head,generalization,tail)
				newSentence = sentence[0]+"<<"+sentence[1]+">>"+sentence[2]
				csv_outData += entry['entityType']+","+entry['entity']+",\""+newSentence+"\"\n"

	with codecs.open("outData/eval/sentences.csv", 'w', 'utf-8') as outputFile:
		outputFile.write(csv_outData)
		outputFile.close()
	return("Great Success!")
	
	
#-------------------------------------------------------
#Selecting a subset of sentences for evaluation
#EDIT: HAS BEEN CHANGED TO ONLY SELECT GENERALIZATIONS
#-------------------------------------------------------	
def selectSomeSentences():
	data = getData() #this is a list of lists of dictionaries
	csv_outData = "TYPE,ENTITY,SENTENCE\n"
	
	entityList = []
	typeList = []
	for entries in data:
		for entry in entries: #entry is a dictionary
			if typeList.count(str(entry['entityType']).lower()) >= 20 or entityList.count(str(entry['entity']).lower()) >= 1:
				continue
			else:
				typeList.append(str(entry['entityType']).lower())
				entityList.append(str(entry['entity']).lower())
			for sentence in entry['sentences']:	#each entry has a list of sentences
				#each sentence is a list of (head,generalization,tail)
				#newSentence = sentence[0]+"<<"+sentence[1]+">>"+sentence[2]
				newSentence = sentence[1]
				csv_outData += entry['entityType']+","+entry['entity']+",\""+newSentence+"\"\n"

	with codecs.open("outData/eval/evaluationSet.csv", 'w', 'utf-8') as outputFile:
		outputFile.write(csv_outData)
		outputFile.close()
	return("Great Success!")

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
#	inData = str(sys.argv[1])
#	results = selectAllSentences()
	results = selectSomeSentences()
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
