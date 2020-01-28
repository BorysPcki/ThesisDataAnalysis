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
    plt.figure(figsize=(20, 5), dpi=100)
    plt.scatter(list(range(len(data))), data)
    plt.title('Entropy')
    plt.xlabel('k')
    # plt.ylim(2.35, 2.55)
    plt.ylabel('S')
    plt.grid()
    plt.savefig(save_path)
    plt.show()


def plot3d(data, save_path):
    plot_data = np.array(data)
    length = plot_data.shape[0]
    width = plot_data.shape[1]
    x, y = np.meshgrid(np.arange(width), np.arange(length))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(y, x, plot_data)
    plt.title('Entropy3D')
    ax.set_xlabel('i')
    ax.set_ylabel('n')
    ax.set_zlabel('S')
    # ax.set_zlim3d(2.35, 2.55)
    plt.savefig(save_path, dpi=100)
    plt.show()


def plot_triple(data, save_path):
    plt.figure(figsize=(20, 5), dpi=100)
    plt.scatter(list(range(len(data[0]))), data[0], label='Puste')
    plt.scatter(list(range(len(data[1]))), data[1], label='Same drożdże')
    plt.scatter(list(range(len(data[2]))), data[2], label='UV')
    plt.legend(loc='upper right')
    plt.xlabel('k')
    plt.ylim(2.5, 3)
    plt.ylabel('S')
    plt.grid()
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


def plot3d_multiple(data, save_path):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for k in range(len(data)):
        plot_data = np.array(data[k])
        length = plot_data.shape[0]
        width = plot_data.shape[1]
        x, y = np.meshgrid(np.arange(width), np.arange(length))
        if k == 0:
            ax.scatter3D(y, x, plot_data, label='Puste')
        elif k == 1:
            ax.scatter3D(y, x, plot_data, label='Same drożdże')
        elif k == 2:
            ax.scatter3D(y, x, plot_data, label='UV')
        else:
            ax.scatter3D(y, x, plot_data, label=k+1)
    ax.set_xlabel('i')
    ax.set_ylabel('n')
    ax.set_zlabel('S')
    ax.set_zlim3d(2.5, 3)
    plt.savefig(save_path, bbox_inches='tight', dpi=100)
    plt.legend(loc='upper right')
    plt.show()
