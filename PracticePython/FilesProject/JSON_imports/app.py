import json

file = open('PracticePython/FilesProject/JSON_imports/data.json', 'r')
json_data = json.load(file)
file.close()

print(json_data["friends"][0])

# how to write to a json data file
cars = {
    "cars": [
        {
            "model": "Ford Fiesta",
            "make": "Ford"
        },

        {
            "model": "Ford Mustang GT",
            "make": "Ford"
        },

        {
            "model": "Hyundai Verna",
            "make": "Hyundai"
        }
    ]
}

#using the dump method, write the cars json data to a cars json file
file = open('PracticePython/FilesProject/JSON_imports/cars_json.json', 'w')
json.dump(cars, file)
file.close()

print('Write completed. Please check file if data was proper.')
