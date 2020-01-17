import csv
import os

from algorithms import entropy
from util import handle_path

folder = ['16.01.2020_17.31', '16.01.2020_18.17']
data2d = []
# data3d = []

for k in range(len(folder)):
    n = 10
    bins = 20
    path = handle_path.HandlePath()
    path.plot_entropy(folder[k], n, bins)

    entropy_plot_data = []

    print(path.input_file_path)
    with open(path.input_file_path) as fileCSV:
        reader_csv = csv.reader(fileCSV)
        entropy_sum = [row for row in reader_csv]

    for i in range(len(entropy_sum)):
        for j in range(len(entropy_sum[0])):
            entropy_sum[i][j] = round(float(entropy_sum[i][j]), 4)
            entropy_plot_data.append(entropy_sum[i][j])
    data2d.append(entropy_plot_data)
    # data3d.append(entropy_sum)

entropy_plot_name = 'entropy_plot.png'
# entropy_plot3d_name = 'entropy_plot3d.png'
output_path = os.path.join(path.path, 'plots')
if not os.path.exists(output_path):
    os.mkdir(output_path)
entropy.plot_triple(data2d, os.path.join(output_path, entropy_plot_name))
# entropy.plot3d_multiple(data3d, os.path.join(output_path, entropy_plot3d_name))
