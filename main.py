import matplotlib.pyplot as plt

from algorithms import entropy
from prepare_data import read_data

data = read_data.ProcessedData('processed_data/test2.csv')
data.read()

plt.plot(data.x, data.y)
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.grid()
plt.show()

plt.plot(data.x[:100000 - 1], data.y[:100000 - 1])
plt.plot(data.x[100000:200000 - 1], data.y[100000:200000 - 1])
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.grid()
plt.show()

plt.plot(data.x, data.y)
plt.xlabel("t [s]")
plt.ylabel("U [V]")
# plt.xlim(0, 0.01)
plt.xlim(0.7, 0.8)
plt.grid()
plt.show()

entropy.entropy_of_k(data.x, data.y, 8, 15)
# meanvalue.mean_of_n_with_step_k(data.y, 10000, 1000)
