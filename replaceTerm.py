import sys
import pprint

#-------------------------------------------------------
#This program takes a term, text, and two positions
#It replaces what is between the two positions with the term
#It then returns the sentence in which the replacement was done
#
#Note: the file has been changed to return a list instead of a string
#The list makes it easier to highlight the replaced term
#
#I repeat, it does not return the entire text
#-------------------------------------------------------
def replaceTerm(term, text, start, stop):
	head = text[:int(start)].rsplit('\n', 1)[-1]
	tail = text[int(stop):].split('\n', 1)[0]
#	sentence = head+term+tail
	sentence = (head,term,tail)
	
	return sentence

#-------------------------------------------------------
#FOR RUNNING AS A SEPARATE PROGRAM (or testing)
#-------------------------------------------------------
if __name__ == "__main__":
	term = str(sys.argv[1])
	text = str(sys.argv[2])
	start = str(sys.argv[3])
	stop = str(sys.argv[4])
	results = replaceTerm(term, text, start, stop)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(results)
