import matplotlib.pyplot as plt
from prepare_data import process_data
from algorithms import meanvalue, entropy

data = process_data.Data('input_data/test2.csv')
data.display_data(10)
value = data.return_data()

plt.plot(data.x, data.y)
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.xlim(0.7, 0.8)
plt.grid()
plt.show()
