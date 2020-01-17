import os

from prepare_data import byte_data
from util import handle_path
import zstandard as zstd


def read(data, start, stop):
    result = ''
    for i in range(start, stop):
        result += format(data[i], '02x') + ' '
    return result


def read_dec(data, start, stop):
    characters = ''
    for i in range(start, stop):
        characters += str(data[i]) + ' '
    return characters


name = '10.01.2020_19.24_dict_64_16'
path = handle_path.HandlePath()
path.read_dict(name)
dict_data = byte_data.read(path.input_file_path)
# dict_data = byte_data.read('X:\\Studia\\III rok\\VI semestr\\Inżynierka\\ThesisDataAnalysis\\output_data\\19.45_03.01.2020_dict_64_16')

dictionary = zstd.ZstdCompressionDict(dict_data)
print(dictionary.dict_id())

data_size = os.path.getsize(path.input_file_path)
print(data_size)

print('Dict length: ', len(dict_data))
magic_number = read(dict_data, 0, 4)
print(magic_number)
magic_number_dec = read_dec(dict_data, 0, 4)
print(magic_number_dec)
dict_id = read(dict_data, 4, 8)
print(dict_id)
rest = read(dict_data, 4, 149)
print(rest)
dec = read_dec(dict_data, 4, 149)
print(dec)
print(dict_data[len(dict_data)-1])