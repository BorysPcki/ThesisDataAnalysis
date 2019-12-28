import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat


def histogram(y, bins):
    return np.histogram(y, bins=bins, density=True)


def entropy_of_k(x, y, k, bins):
    x = np.array_split(x, k)
    y = np.array_split(y, k)
    for j in range(k):
        plt.plot(x[j], y[j])
    plt.grid()
    plt.show()
    entropy = []
    for j in range(k):
        h = histogram(y[j], bins)
        entropy.append(stat.entropy(h[0]))
        if j == k - 1:
            plt.plot(list(range(bins)), h[0])
            plt.title('Last histogram')
            plt.grid()
            plt.show()
    plt.scatter(list(range(k)), entropy)
    plt.title('Entropy')
    plt.xlabel('k')
    plt.ylabel('value')
    plt.grid()
    plt.show()
