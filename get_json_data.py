#create table

import extract_sentence
from get_mysql_data import getBookWords



def read_text_file(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split()
        return words

    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    
        
        
def get_list_from_file(search_file_path):
    search_list = read_text_file(search_file_path)       
    search_list.sort()
    return search_list

#print(search_list)



#print(search_list)
#search_file_path = "LIST001.txt"
#search_list = get_list_from_file(search_file_path)

BOOK_ID = 1

search_list = getBookWords(BOOK_ID)


in_file_path = "pdf_extract.txt"
out_file_path = "sentences.json"

result = extract_sentence.searchAll(in_file_path, search_list, out_file_path)

if result == 0:
	print ("Sucessfully done!")

 
