import os

from prepare_data import byte_data

folder = '17.01.2020_20.16'
processed_up_path = 'V:\\thesis\\processed_data'
processed_path = os.path.join(processed_up_path, folder)
input_files = os.listdir(processed_path)

samples = byte_data.convert(processed_path, input_files)
byte_data.save(samples, os.path.join(processed_up_path, folder + '_byte'))
