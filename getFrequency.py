import urllib, urllib2, base64, json
import sys

def getFrequency(term):
#-------------------------------------------------------
#CREATING URL FOR SKETCH ENGINE QUERY
#LAYOUT OF FILE LARGELY STOLEN FOM SKETCH ENGINE TUTORIAL PAGES
#-------------------------------------------------------
	base_url = 'http://localhost/bonito/run.cgi/'
	method = 'view'
	
	attrs = dict(corpname='nature_full_v2', q=' ', pagesize='1', format='json')

	queryList=[]
#-------------------------------------------------------
#SETTING LAST WORD IN TERM AS LEMMA
#REMAINING WORDS USE EXACT WORD MATCH
#-------------------------------------------------------
	try:
		term = term.split(' ')	
		for word in term:
			queryList.append('[word="(?i)%s"]'%word)
		queryList[-1]='[lemma="(?i)%s"]'%term[-1]
		query = ''.join(queryList)
		attrs['q']= 'q'+query

		encoded_attrs = urllib.quote(json.dumps(attrs))
		url = base_url + method + '?json=%s'%encoded_attrs

		request = urllib2.Request(url)

		# json data receiving
		file = urllib2.urlopen(request)
		data = file.read()
		file.close()	
	
		# parse json from 'data' variable
		json_obj = json.loads(data)
	
	#	print urllib.unquote(url)
	#	print json_obj
	except:
		return 0
#-------------------------------------------------------
#RETURNING THE NUMBER OF OCCURRENCES CAST TO INT
#-------------------------------------------------------
	return (int(json_obj.get('concsize', '0')))
#-------------------------------------------------------
#AS USUAL, THE PARTS BELOW LET YOU RUN THE FILE ON ITS OWN
#-------------------------------------------------------
if __name__ == "__main__":
	word = sys.argv[1]
	result = getFrequency(word)
	print result
