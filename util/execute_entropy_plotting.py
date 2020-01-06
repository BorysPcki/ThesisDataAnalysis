import csv
import os

from algorithms import entropy
from util import handle_path

folder = '18.35_03.01.2020'
n = 10
bins = 20
path = handle_path.HandlePath()
path.plot_entropy(folder, n, bins)

entropy_plot_data = []

print(path.input_file_path)
with open(path.input_file_path) as fileCSV:
    reader_csv = csv.reader(fileCSV)
    entropy_sum = [row for row in reader_csv]

for i in range(len(entropy_sum)):
    for j in range(len(entropy_sum[0])):
        entropy_sum[i][j] = round(float(entropy_sum[i][j]), 4)
        entropy_plot_data.append(entropy_sum[i][j])
print(entropy_sum)
print(entropy_plot_data)

entropy_plot_name = 'entropy_plot.png'
entropy_plot3d_name = 'entropy_plot3d.png'
output_path = os.path.join(path.path, 'plots')
if not os.path.exists(output_path):
    os.mkdir(output_path)
entropy.plot(entropy_plot_data, os.path.join(output_path, entropy_plot_name))
entropy.plot3d(entropy_sum, os.path.join(output_path, entropy_plot3d_name))
