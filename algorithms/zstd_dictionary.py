import os
import zstandard as zstd
from prepare_data import byte_data
from util import handle_path

k = 64
d = 16
name = '19.45_03.01.2020'
path = handle_path.HandlePath()
path.train_dict(name, k, d)
samples = byte_data.read(path.input_file_path)
data_size = os.path.getsize(path.input_file_path)
print(data_size)
size = int(0.1 * data_size)
print(size)

dict_data = zstd.train_dictionary(size, samples, k=k, d=d)
print('Dict size: ', len(dict_data))
print('Dict data type: ', type(dict_data))
raw_dict_data = dict_data.as_bytes()
byte_data.save(raw_dict_data, path.output_file_path)
