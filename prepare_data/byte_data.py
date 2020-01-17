import os
import pickle
import sys

from prepare_data import read_data


def convert(path, files):
    samples = []
    # for i in range(5):
    for i in range(len(files)):
        processed_file = os.path.join(path, files[i])
        data = read_data.ProcessedData(processed_file)
        data.read()
        sample = bytearray()
        # for j in range(int(len(data.y) / 10000)):
        for j in range(len(data.y)):
            data_to_int = int(data.y[j] * (10 ** 7))
            byte = data_to_int.to_bytes(length=4, byteorder=sys.byteorder, signed=True)
            sample += bytearray(byte)
        data.clear_data()
        samples.append(bytes(sample))
    return samples


def save(data, path):
    with open(path, 'wb') as fp:
        pickle.dump(data, fp)


def read(path):
    with open(path, 'rb') as fp:
        read_samples = pickle.load(fp)
    return read_samples
