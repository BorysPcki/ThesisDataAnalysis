import os

import matplotlib.pyplot as plt

from algorithms import entropy, meanvalue
from prepare_data import read_data

folder = '19.45_03.01.2020'
processed_path = os.path.join('V:\\thesis\\processed_data', folder)
input_files = os.listdir(processed_path)
project_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(project_path, 'output_data', folder)
os.mkdir(output_path)

entropy_sum = []

for i in range(len(input_files)):
    processed_file = os.path.join(processed_path, input_files[i])
    data = read_data.ProcessedData(processed_file)
    data.read()
    entropy_part = entropy.calculate_from_file(data.x, data.y, 10, 20)
    for j in range(len(entropy_part)):
        entropy_sum.append(entropy_part[j])

entropy_plot_name = 'entropy_plot.png'
entropy.plot(entropy_sum, os.path.join(output_path, entropy_plot_name))
# meanvalue.mean_of_n_with_step_k(data.y, 10000, 1000)
