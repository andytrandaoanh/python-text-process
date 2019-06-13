
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




in_file_path = "pdf_extract.txt"


input_text = readTextFile(in_file_path)	

output = tokenize.sent_tokenize(input_text)

total = len(output)
#print ('total sentences: ', total)
search_string = 'abdicate'

pat = re.compile(search_string, re.IGNORECASE)



index = 0
result =[]
for sentence in output:	
	matchObject = re.search(pat, sentence)
	if (matchObject):
		print(matchObject)
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


print(len(result))