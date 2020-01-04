import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stat


def histogram(y, bins):
    return np.histogram(y, bins=bins, density=True)


def calculate_from_file(x, y, k, bins):
    x = np.array_split(x, k)
    y = np.array_split(y, k)
    entropy = []
    for j in range(k):
        h = histogram(y[j], bins)
        entropy.append(stat.entropy(h[0]))

    return entropy


def plot(data, save_path):
    plt.figure(figsize=(20, 4), dpi=100)
    plt.scatter(list(range(len(data))), data)
    plt.title('Entropy')
    plt.xlabel('k')
    plt.ylabel('value')
    plt.grid()
    plt.savefig(save_path)
    plt.show()
