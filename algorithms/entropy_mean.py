import csv
from statistics import mean, stdev

from util import handle_path

min_limit = 2.5
max_limit = 3
folder = '10.01.2020_20.37'
n = 10
bins = 20
path = handle_path.HandlePath()
path.plot_entropy(folder, n, bins)

entropy = []

with open(path.input_file_path) as fileCSV:
    reader_csv = csv.reader(fileCSV)
    entropy_sum = [row for row in reader_csv]

for i in range(25, len(entropy_sum)):
    for j in range(len(entropy_sum[0])):
        entropy_sum[i][j] = round(float(entropy_sum[i][j]), 4)
        if min_limit < entropy_sum[i][j] < max_limit:
            entropy.append(entropy_sum[i][j])

print(round(mean(entropy), 3), ';', round(stdev(entropy), 3))
