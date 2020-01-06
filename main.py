import csv
import os

from algorithms import entropy
from prepare_data import read_data
from util import handle_path

folder = '19.21_03.01.2020_no_uv'
n = 10
bins = 20
path = handle_path.HandlePath()
path.calculate_entropy(folder, n, bins)


entropy_plot_data = []
entropy_sum = []

for i in range(len(path.input_files)):
    print(path.input_files[i])
    processed_file = os.path.join(path.processed_path, path.input_files[i])
    data = read_data.ProcessedData(processed_file)
    data.read()
    entropy_part = entropy.calculate_from_file(data.x, data.y, n, bins)
    entropy_sum.append(entropy_part)
    for j in range(len(entropy_part)):
        entropy_plot_data.append(entropy_part[j])
    data.clear_data()

with open(os.path.join(path.output_sub_path, path.output_file), 'w', newline='') as fileCSV:
    writer_csv = csv.writer(fileCSV, quoting=csv.QUOTE_ALL)
    for i in range(len(entropy_sum)):
        writer_csv.writerow(entropy_sum[i])

entropy_plot_name = 'entropy_plot.png'
entropy_plot3d_name = 'entropy_plot3d.png'
entropy.plot(entropy_plot_data, os.path.join(path.output_sub_path, entropy_plot_name))
entropy.plot3d(entropy_sum, os.path.join(path.output_sub_path, entropy_plot3d_name))
