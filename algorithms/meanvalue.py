from statistics import mean

import matplotlib.pyplot as plt


def mean_of_n_with_step_k(data, n, k):
    mean_list = []
    x = []
    print(len(data) - n)
    for i in range(0, len(data) - n, int(n / k)):
        print(i)
        x.append(i)
        subdata = data[0 + i:n + i]
        mean_list.append(mean(subdata))
        if i == 0 or i == n/k:
            print(subdata)
            print(mean(subdata))
            print()
    plt.plot(x, mean_list)
    plt.grid()
    plt.show()
