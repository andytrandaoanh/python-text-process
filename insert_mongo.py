import datetime
import json
from pymongo import MongoClient
from pprint import pprint

from get_mysql_data import getBookData


client = MongoClient('localhost', 27017)


DB_NAME = 'lexicon'
COLLECTION_NAME = 'examples'
INPUT_JSON_FILE = 'sentences_4.json'
BOOK_ID = 4



dbName = DB_NAME
collectionName = COLLECTION_NAME
fileName = INPUT_JSON_FILE
bookID = BOOK_ID

db = client[dbName]
coll = db[collectionName]


with open(fileName) as f:
    my_dic = json.load(f)



my_book = getBookData(bookID)

#print(my_book)


my_doc = []

for word in my_dic:
	word['book_info'] = my_book
	my_doc.append(word)
	#print(word)
	#example_id = coll.insert_one(word).inserted_id
	#log_data.append(example_id)
	#print(example_id)
	#return log_data


#pprint(my_doc)


x = coll.insert_many(my_doc)

pprint(x)



