import matplotlib.pyplot as plt
from prepare_data import process_data
from algorithms import meanvalue, entropy

data = process_data.Data('input_data/test2.csv')
data.display_data(10)
value = data.return_data()
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

entropy.entropy_of_k(value[0], value[1], 8, 15)
# meanvalue.mean_of_n_with_step_k(data.y, 10000, 1000)
