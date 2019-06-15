import datetime
import json
from pymongo import MongoClient
from pprint import pprint

from get_mysql_data import getBookData


def insertDBOne(doc):
	try:
		
		if doc['key_word']:
		#print(doc['key_word'])
			volumnName = 'vol_' +  doc['key_word'][:1].lower()
			#print (volumnName)
			collection = db[volumnName]
			objid = collection.insert_one(doc).inserted_id
	except Exception as e:
		print('Error: ', e)
	
	#return objid
	#print(objid)

client = MongoClient('localhost', 27017)


DB_NAME = 'lexicon'

INPUT_JSON_FILE = 'sentences_4.json'
BOOK_ID = 4



dbName = DB_NAME
fileName = INPUT_JSON_FILE
bookID = BOOK_ID

db = client[dbName]



with open(fileName) as f:
    my_dic = json.load(f)



my_book = getBookData(bookID)

#print(my_book)



my_index = 0

"""
single_word = {}
my_index += 1
word = my_dic[0]
single_word['doc_id'] = my_index
single_word['key_word'] = word['key-word']
single_word['book_info'] = my_book
single_word['sentences'] = word['sentences']
insertDBOne(single_word)
"""

#print(single_word)


for word in my_dic:
	single_word = {}
	my_index += 1
	#word = my_dic[0]
	single_word['doc_id'] = my_index
	single_word['book_info'] = my_book
	single_word['key_word'] = word['key-word']
	single_word['sentences'] = word['sentences']
	insertDBOne(single_word)
	#print(objid)

	#print(single_word)


#	my_index += 1
#	sing_word = {}
	#sing_word['doc_id'] = my_index
	#sing_word['book_info'] = my_book

	
#	my_doc.append(word)
#	print(word)
	#example_id = coll.insert_one(word).inserted_id
	#log_data.append(example_id)
	#print(example_id)
	#return log_data
	



#pprint(my_doc)


#x = coll.insert_many(my_doc)

#pprint(x)



