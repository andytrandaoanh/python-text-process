#create table
import extract_sentence
from get_mysql_data import getBookWords

BOOK_ID = 4

search_list = getBookWords(BOOK_ID)


#print(search_list)

#print(search_list)

in_file_path = "E:/FULLTEXT/INPUT/BOOK_004_Sapiens_A_Brief_History.txt"
out_file_path = "sentences_4.json"

result = extract_sentence.searchAll(in_file_path, search_list, out_file_path)

if result == 0:
	print ("Sucessfully done!")

 
