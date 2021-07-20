import json

with open('PracticePython/FilesProject/JSON_imports/data.json', 'r') as file:
    json_data = json.load(file)
    print(json_data)
