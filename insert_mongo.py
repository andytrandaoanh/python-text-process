import datetime
import json
from pymongo import MongoClient

from get_mysql_data import getBookData


client = MongoClient('localhost', 27017)


DB_NAME = 'lexicon'
COLLECTION_NAME = 'examples'

db = client[DB_NAME]
coll = db[COLLECTION_NAME]


file_name = 'sentences.json'


with open(file_name) as f:
    my_dic = json.load(f)


#my_book = { 'book_id' :1,
#	'book_title':	'The First-Time Manager',
#	'book_author' :	'Loren B. Belke',
#	'book_year' :	2012}

my_book = getBookData(1)

#print(my_book)



for word in my_dic:
	word['book_info'] = my_book
	#print(word)
	example_id = coll.insert_one(word).inserted_id
	print(example_id)









