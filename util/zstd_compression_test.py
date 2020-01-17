import os
import sys

import zstandard as zstd

from prepare_data import read_data

folder = '10.01.2020_19.35'
processed_up_path = 'V:\\thesis\\processed_data'
processed_path = os.path.join(processed_up_path, folder)
input_files = os.listdir(processed_path)

sample = bytearray()
for i in range(len(input_files)):
    processed_file = os.path.join(processed_path, input_files[i])
    data = read_data.ProcessedData(processed_file)
    data.read()
    # for j in range(int(len(data.y) / 10000)):
    for j in range(len(data.y)):
        data_to_int = int(data.y[j] * (10 ** 7))
        byte = data_to_int.to_bytes(length=4, byteorder=sys.byteorder, signed=True)
        sample += bytearray(byte)
    data.clear_data()

cctx = zstd.ZstdCompressor()
compressed = cctx.compress(sample)
print(sys.getsizeof(sample))
print(len(sample))
print(sys.getsizeof(compressed))
print(len(compressed))
