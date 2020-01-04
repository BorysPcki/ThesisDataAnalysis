import matplotlib.pyplot as plt

from prepare_data import read_data

data = read_data.ProcessedData('processed_data/16.00_03.01.2020_test_ukladu.csv')
data.read()

plt.plot(data.x, data.y)
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.xlim(0.7, 0.8)
plt.grid()
plt.show()
