import os
import sys

import zstandard as zstd

from prepare_data import read_data

folder = '19.45_03.01.2020'
processed_path = os.path.join('V:\\thesis\\processed_data', folder)
input_files = os.listdir(processed_path)
data_to_compress = bytearray()

# for i in range(len(input_files)):
for i in range(2):
    processed_file = os.path.join(processed_path, input_files[i])
    data = read_data.ProcessedData(processed_file)
    data.read()
    for j in range(len(data.y)):
        data_to_int = int(data.y[j] * (10 ** 7))
        byte = data_to_int.to_bytes(length=3, byteorder=sys.byteorder, signed=True)
        data_to_compress += bytearray(byte)
    data.clear_data()


print('size precompress: ', sys.getsizeof(data_to_compress))
cctx = zstd.ZstdCompressor()
compressed = cctx.compress(data_to_compress)
# print('compressed: ', compressed)
print('size compress: ', sys.getsizeof(compressed))

dctx = zstd.ZstdDecompressor()
decompressed = dctx.decompress(compressed)
print('size decompress: ', sys.getsizeof(decompressed))
