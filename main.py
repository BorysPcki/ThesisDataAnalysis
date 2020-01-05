import csv
import os

from algorithms import entropy
from prepare_data import read_data

folder = '18.35_03.01.2020'
n = 10
bins = 50
sub_folder = 'entropy_' + str(n) + '-' + str(bins)
output_file = sub_folder + '.csv'
processed_path = os.path.join('V:\\thesis\\processed_data', folder)
input_files = os.listdir(processed_path)
project_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(project_path, 'output_data', folder)
# output_path = os.path.join('V:\\thesis\\test', folder)
if not os.path.exists(output_path):
    os.mkdir(output_path)
output_sub_path = os.path.join(project_path, 'output_data', folder, sub_folder)
if not os.path.exists(output_sub_path):
    os.mkdir(output_sub_path)

entropy_plot_data = []
entropy_sum = []

for i in range(len(input_files)):
    processed_file = os.path.join(processed_path, input_files[i])
    data = read_data.ProcessedData(processed_file)
    data.read()
    entropy_part = entropy.calculate_from_file(data.x, data.y, n, bins)
    entropy_sum.append(entropy_part)
    for j in range(len(entropy_part)):
        entropy_plot_data.append(entropy_part[j])

with open(os.path.join(output_sub_path, output_file), 'w', newline='') as fileCSV:
    writer_csv = csv.writer(fileCSV, quoting=csv.QUOTE_ALL)
    for i in range(len(entropy_sum)):
        writer_csv.writerow(entropy_sum[i])

entropy_plot_name = 'entropy_plot.png'
entropy_plot3d_name = 'entropy_plot3d.png'
entropy.plot(entropy_plot_data, os.path.join(output_sub_path, entropy_plot_name))
entropy.plot3d(entropy_sum, os.path.join(output_sub_path, entropy_plot3d_name))
