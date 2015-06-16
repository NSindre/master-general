from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer
import pprint
import sys

#-------------------------------------------------------
#NLTK LEMMATIZATION, ONLY LEMMATIZES FINAL WORD IN TERM
#-------------------------------------------------------
def lemmatize(term):
	lemmatizer = WordNetLemmatizer()
	words = term.split(' ')
	words[-1] = lemmatizer.lemmatize(words[-1].lower())
	lemma = ' '.join(words)
	return lemma
#-------------------------------------------------------
#OTHER (OLD) FUNCTIONS:
#STEMMING IS OFTEN TOO AGRESSIVE, CUTTING AWAY MORE THAN IT SHOULD
#THIS FUNCTION STEMS ONLY IF LEMMATIZATION DOES NOTHING
#
#BEFORE USE: CHANGE TO STEM/LEMMATIZE ONLY LAST WORD IN TERM 
#-------------------------------------------------------
def stemLem(w):
	lemmatizer = WordNetLemmatizer()
	stemmer = SnowballStemmer("english")
	#stemmer = PorterStemmer()

	lem = lemmatizer.lemmatize(w)
	if len(w) > len(lem):
		return lem
	return stemmer.stem(w)
#-------------------------------------------------------
#THIS VERY NAIVE FUNCTION REMOVES ANY TRAILING 'S'
#-------------------------------------------------------
def unTrailS(w):
	return w.rstrip('s')

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM
#-------------------------------------------------------
if __name__ == "__main__":
	qInputVariable = str(sys.argv[1])
	print(qInputVariable +": ")
	results = lemmatize(qInputVariable)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
