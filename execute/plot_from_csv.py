import csv
import matplotlib.pyplot as plt

path = 'V:\\thesis\\bandwidth_characteristic.csv'
save_path = 'V:\\thesis\\bandwidth_characteristic.png'
with open(path) as fileCSV:
    reader_csv = csv.reader(fileCSV, delimiter=';')
    data = [row for row in reader_csv]

x = []
y = []
for i in range(len(data)):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))

plt.figure(figsize=(7, 5), dpi=100)
plt.scatter(x, y)
plt.xlabel('f [kHz]')
plt.xscale('log')
plt.ylabel('U [V]')
plt.grid()
plt.savefig(save_path, bbox_inches='tight')
plt.show()
