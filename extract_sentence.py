#filepath = "C:/Users/administrator.DIGINETCORP/Dropbox/FULLTEXT PROJECT/6-habits-of-Highly-Effective-Bosses.txt"

import re
from nltk import tokenize
import json



def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)    
	    
def cleanText(input_text):	    
	line = input_text
	line = line.replace('\n',' ')
	line = line.replace('\t',' ')
	return line

def getSencences(input_text, text_to_search):
	result = []
	output = tokenize.sent_tokenize(input_text)

	total = len(output)
	#print ('total sentences: ', total)
	search_string = text_to_search

	pat = re.compile(search_string, re.IGNORECASE)
	index = 0
	for sentence in output:	
		matchObject = re.search(pat, sentence)
		if (matchObject):
			if (index == 0):
				if (total == 1):
					result.append([cleanText(output[index])])
				elif (total > 1):
					result.append([cleanText(output[index]) +  ' ' + cleanText(output[index+1])])
			elif (index > 0):
				if (index + 1 <= total):
					result.append([cleanText(output[index-1]) + ' ' +  cleanText(output[index])])
				elif (index + 1 > total):
					result.append([cleanText(output[index-1]) + ' ' + cleanText(output[index]) +' ' +  CleanText(output[index+1])])

			#print(index, sentence)
		index += 1
	return result







def searchSingle(mytext, text_to_search):
	

	my_sentences = getSencences(mytext, text_to_search )

	if (len(my_sentences) > 0):
		my_data = {
			"key-word": text_to_search,
			"sentences": my_sentences
			}
	else:
		my_data = None

	return my_data


def searchAll(in_file_path, search_list, out_file_path):
	data_out = []
	mytext = readTextFile(in_file_path)	

	for search_text in search_list:
		#print(search_text)
		single_search = searchSingle(mytext, search_text)
		if(single_search):
			print('match found: ', search_text)
			data_out.append(single_search)


	with open(out_file_path, 'w', encoding ="utf-8") as outfile:  
	    json.dump(data_out, outfile)

	return 0
