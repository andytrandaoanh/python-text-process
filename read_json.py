import json

file_name = 'sentences.json'


with open(file_name) as f:
    d = json.load(f)
    print(d)



    