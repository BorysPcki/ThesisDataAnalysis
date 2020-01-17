import csv
import os

from prepare_data import process_data

folder = '16.01.2020_18.17'
input_path = os.path.join('V:\\thesis\\raw_data', folder)
processed_path = os.path.join('V:\\thesis\\processed_data', folder)
if not os.path.exists(processed_path):
    os.mkdir(processed_path)
input_files = os.listdir(input_path)

for n in range(len(input_files)):
    input_file = os.path.join(input_path, input_files[n])
    # processed_file = os.path.join(processed_path, input_files[n])
    processed_file = os.path.join(processed_path, input_files[n])
    data = process_data.Data(input_file)
    data.append_data()

    with open(processed_file, 'w', newline='') as fileCSV:
        writer_csv = csv.writer(fileCSV, quoting=csv.QUOTE_ALL)
        for i in range(len(data.x)):
            writer_csv.writerow([data.x[i], data.y[i]])
    data.clear_data()
