import os
import sys

import zstandard as zstd
from prepare_data import byte_data
from util import handle_path

k = 64
d = 16
name = '10.01.2020_19.24'
path = handle_path.HandlePath()
path.train_dict(name, k, d)
samples = byte_data.read(path.input_file_path)
data_size = sys.getsizeof(samples[0])
print(data_size)
# size = 1024
size = int(0.1 * data_size)
# size = int(0.01 * data_size)
print(size)

dict_data = zstd.train_dictionary(size, samples, k=k, d=d, dict_id=0x27BC86AA)
print('Dict size: ', len(dict_data))
print('Dict data type: ', type(dict_data))
raw_dict_data = dict_data.as_bytes()
byte_data.save(raw_dict_data, path.output_file_path)
# byte_data.save(raw_dict_data, 'V:\\thesis\\10.01.2020_19.35_25_small')
