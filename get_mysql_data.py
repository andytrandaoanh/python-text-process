#create table

import mysql.connector
import dbconnect2
from mysql.connector import errorcode



#return tuple
#(1, 'The First-Time Manager', 'Loren B. Belke', 2012)



def getBookData(book_id):
	DB_NAME = "lexicon"
	db = dbconnect2.get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select * from books where book_id = " + str(book_id) +";")
	try:
		cursor.execute(select_sql)
		record = cursor.fetchone()
		return formatBookInfo(record, cursor.description)
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close
	



def formatBookInfo(record, description):
#((1, 'The First-Time Manager', 'Loren B. Belke', 2012), [('book_id', 3, None, None, None, None, 0, 53251), ('book_title', 253, None, None, None, None, 1, 0), ('book_author', 253, None, None, None, None, 1, 0), ('book_year', 2, None, None, None, None, 1, 32768)])
		#expression for item in list
	field_names  = [item[0] for item in description]

	book_info = {}

	index = 0

	for field in field_names:
		book_info[field] = record[index]
		index += 1

	return book_info




def getBookWords(book_id):
	DB_NAME = "lexicon"
	db = dbconnect2.get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select word_form from words where book_id = " + str(book_id) +";")
	try:
		cursor.execute(select_sql)
		record = cursor.fetchall()
		word_list  = [item[0] for item in record]
		return word_list
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close


def main():
	my_words = getBookWords(1)
	print(my_words)