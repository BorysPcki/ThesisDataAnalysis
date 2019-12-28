import numpy
import matplotlib.pyplot as plt
from algorithms import meanvalue

mean = 0
std = 1
num_samples = 1000
samples = numpy.random.normal(mean, std, size=num_samples)

plt.plot(samples)
plt.grid()
plt.show()
meanvalue.mean_of_n_with_step_k(samples, 100, 10)
