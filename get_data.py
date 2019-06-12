#create table

import extract_sentence




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
        
        
search_file_path = "LIST001.txt"

search_list = read_text_file(search_file_path)        

#print(search_list)



#print(search_list)

in_file_path = "pdf_extract.txt"
out_file_path = "sentences.json"

result = extract_sentence.searchAll(in_file_path, search_list, out_file_path)

if result == 0:
	print ("Sucessfully done!")

 
