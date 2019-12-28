import csv
import os

from prepare_data import process_data

project_path = os.path.dirname(os.path.dirname(__file__))
input_path = project_path + '/input_data/test2.csv'
processed_path = project_path + '/processed_data/test2.csv'

data = process_data.Data(input_path)
data.display_data(10)
data.append_data()

with open(processed_path, 'w', newline='') as fileCSV:
    writer_csv = csv.writer(fileCSV, quoting=csv.QUOTE_ALL)
    for i in range(len(data.x)):
        writer_csv.writerow([data.x[i], data.y[i]])
