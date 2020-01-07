import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.stats as stat


def histogram(y, bins):
    return np.histogram(y, bins=bins, density=True)


def calculate_from_file(x, y, n, bins):
    x = np.array_split(x, n)
    y = np.array_split(y, n)
    entropy = []
    for j in range(n):
        h = histogram(y[j], bins)
        entropy.append(round(stat.entropy(h[0]), 4))

    return entropy


def plot(data, save_path):
    plt.figure(figsize=(20, 4), dpi=100)
    plt.scatter(list(range(len(data))), data)
    plt.title('Entropy')
    plt.xlabel('k')
    # plt.ylim(2.15, 2.45)
    plt.ylabel('value')
    plt.grid()
    plt.savefig(save_path)
    plt.show()


def plot3d(data, save_path):
    plot_data = np.array(data)
    length = plot_data.shape[0]
    width = plot_data.shape[1]
    x, y = np.meshgrid(np.arange(length), np.arange(width))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(x, y, plot_data)
    plt.title('Entropy3D')
    ax.set_xlabel('i')
    ax.set_ylabel('n')
    ax.set_zlabel('value')
    # ax.set_zlim3d(2.15, 2.45)
    plt.savefig(save_path, dpi=100)
    plt.show()
