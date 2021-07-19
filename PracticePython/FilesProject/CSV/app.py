csv_data = open('PracticePython/FilesProject/CSV/csv_data.txt', 'r')

csv_list = [data.strip() for data in csv_data]
print(csv_list[1:])

csv_data.close()