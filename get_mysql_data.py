#create table

import mysql.connector
import dbconnect2
from mysql.connector import errorcode
import extract_sentence




DB_NAME = "lexicon"

db = dbconnect2.get_connection(DB_NAME)

cursor = db.cursor()

select_sql= ("select * from pure_words order by word_form;")

cursor.execute(select_sql)
records = cursor.fetchall()
search_list=[]
for row in records:
	search_list.append(row[0])
cursor.close()
db.close()


#print(search_list)

in_file_path = "pdf_extract.txt"
out_file_path = "sentences.json"

result = extract_sentence.searchAll(in_file_path, search_list, out_file_path)

if result == 0:
	print ("Sucessfully done!")

 
