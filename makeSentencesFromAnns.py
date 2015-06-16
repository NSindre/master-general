import sys
import os.path
import codecs
import glob
import pprint
from replaceTerm import replaceTerm
from getTermRecords import getTermRecords
try:
	import cPickle as pickle
except:
	import pickle
#-------------------------------------------------------
#This is a dictionary, it stores all the info gathered below
#-------------------------------------------------------
def dataSetDict():
	ds = dict(
		entity = "",
		entityType = "",
		generalizations = [],
		sentences = [],
		fileName = "",
		)
	return ds

def makeSentences():
#-------------------------------------------------------
#Opening all annotation and text files in a directory
#-------------------------------------------------------
	annsDir = "inData/anns/"
	for filename in glob.glob(annsDir+'*.ann'):
		filenameStripped = filename.rsplit('.',1)[0].replace(annsDir,'')
		newDataFile = 'outData/replSentences/'+filenameStripped+'.rpls'
		if os.path.isfile(newDataFile):
			continue	#Skipping files that are already done (because it is lame to start over)
		with codecs.open(filename, 'r', 'utf-8') as annotation:
			with codecs.open(filename.rsplit('.',1)[0]+'.txt', 'r', 'utf-8') as text:
				textString = text.read()
				ann_data = []
				for line in annotation:
					ann_data.append(line.split(None,4))
#-------------------------------------------------------
#Creating list of dictionaries for every file
#-------------------------------------------------------
		dataSetList = [] #Container for storing all the data sets
		for ann in ann_data:
			dataSet = dataSetDict()
			dataSet['fileName']=filenameStripped
			dataSet['entity'] = ann[4].strip()
			dataSet['entityType'] = ann[1].strip()
			termRecords = getTermRecords(dataSet['entityType'],dataSet['entity'])

			#very sexy line of code follows
			#it adds to the list only generalizations that both appear in text corpus
			#and is not equal to the initial term (eliminates very many bad generalizations)
			#dataSet['generalizations'].append(termData['generalizedLabel'] for termData in termRecords if termData['generalizedFreq'] >= 1 and termData['generalizedLabel']!=dataSet['entity'])
			#sadly, I could not pickle a generator, so the sexy code remains as a reminder
			
			for termData in termRecords:
				if termData['generalizedFreq']	>= 1 and termData['generalizedLabel'].lower() != dataSet['entity'].lower():
					dataSet['generalizations'].append(termData['generalizedLabel'])

			dataSet['generalizations'] = list(set(dataSet['generalizations'])) #this removes duplicates
			for gen in dataSet['generalizations']:	#this removes near duplicates
				try:
					dataSet['generalizations'].remove(gen+"s")
				except:
					pass
				try:
					dataSet['generalizations'].remove((gen+"s").capitalize())
				except:
					pass
				try:
					dataSet['generalizations'].remove((gen+"s").lower())
				except:
					pass
				try:
					if gen[0].islower(): dataSet['generalizations'].remove(gen.capitalize())
				except:
					pass
			#dataSet['sentences'].append(replaceTerm(gen,textString,ann[2],ann[3]) for gen in dataSet['generalizations'])
			for gen in dataSet['generalizations']:
				dataSet['sentences'].append(replaceTerm(gen,textString,ann[2],ann[3]))

			dataSetList.append(dataSet)
#-------------------------------------------------------
#Writing to outData and returning
#-------------------------------------------------------
		with open(newDataFile, 'wb') as recordFile:
			print("Saving record to: "+newDataFile)
			pickle.dump(dataSetList, recordFile)
	return("Congratulations, this probably took a while.")
#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	results = makeSentences()
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
