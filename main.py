#create table
import extract_sentence

#print(search_list)

in_file_path = "pdf_extract.txt"
out_file_path = "sentences.json"

result = extract_sentence.searchAll(in_file_path, search_list, out_file_path)

if result == 0:
	print ("Sucessfully done!")

 
