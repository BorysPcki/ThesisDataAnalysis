import csv
import os

import matplotlib.pyplot as plt
import scipy.stats as stat

x = []
y = []
file = '17.01.2020_20.16_dict_64_16'
path = 'V:\\thesis\\dict\\0,1'
with open(os.path.join(path, file + '.csv')) as fileCSV:
    reader_csv = csv.reader(fileCSV, delimiter=' ')
    for row in reader_csv:
        x.append(row[0])
        y.append(row[1])

temp = []
unique = []
for i in range(len(x)):
    if [x[i], y[i]] not in temp:
        temp.append([x[i], y[i]])
        unique.append(x[i])

histogram_unique = {}
for v in unique:
    if v not in histogram_unique:
        histogram_unique[v] = 0
        histogram_unique[v] += 1
    else:
        histogram_unique[v] += 1
if '6' not in histogram_unique:
    histogram_unique[6] = 0

histogram = {}
for v in x:
    if v not in histogram:
        histogram[v] = 0
        histogram[v] += 1
    else:
        histogram[v] += 1
if '6' not in histogram:
    histogram[6] = 0

bar_width = 0.4
histogram_x = list(histogram.keys())
histogram_x = [int(x) for x in histogram_x]
ticks = histogram_x
histogram_x = [x + bar_width / 2 for x in histogram_x]
histogram_y = list(histogram.values())
histogram_unique_x = list(histogram_unique.keys())
histogram_unique_x = [int(x) - bar_width / 2 for x in histogram_unique_x]
histogram_unique_y = list(histogram_unique.values())
plt.bar(histogram_x, histogram_y, width=bar_width, color='c', label='słowa')
plt.bar(histogram_unique_x, histogram_unique_y, width=bar_width, color='b', label='słowa unikalne')
for i in range(len(histogram_x)):
    plt.text(x=histogram_x[i] - 0.05, y=histogram_y[i] + 2, s=histogram_y[i], size=10, color='c', weight='bold')
    plt.text(x=histogram_unique_x[i] - 0.05, y=histogram_unique_y[i] + 2, s=histogram_unique_y[i], size=10, color='b',
             weight='bold')
plt.ylim(0, 500)
plt.xticks(ticks)
plt.xlabel('długość bitowa')
plt.ylabel('liczba słów')
plt.legend(loc='upper left')
# plt.savefig(os.path.join(path, file + '.png'), dpi=100)
plt.show()

print(histogram_y)
print(histogram_unique_y)
entropy = round(stat.entropy(histogram_y), 4)
print('all:', entropy)
entropy_unique = round(stat.entropy(histogram_unique_y), 4)
print('unique:', entropy_unique)