from prepare_data import byte_data
from util import handle_path


def read(start, stop):
    result = ''
    for i in reversed(range(start, stop)):
        # result += hex(dict_data[i]).split('x')[-1]
        result += format(dict_data[i], 'x') + ' '
    return result


name = '18.35_03.01.2020_dict_64_16'
path = handle_path.HandlePath()
path.read_dict(name)
dict_data = byte_data.read(path.input_file_path)

magic_number = read(0, 4)
print(magic_number)
dict_id = read(4, 8)
print(dict_id)
rest = read(8, 156)
print(rest)
