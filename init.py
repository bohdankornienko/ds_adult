import os
import urllib.request

this_dir = os.path.dirname(os.path.realpath(__file__))

url_prefix = 'http://archive.ics.uci.edu/ml/machine-learning-databases/adult/'

remote_files = {
        'data' : url_prefix + 'adult.data',
        'test' : url_prefix + 'adult.test',
        'info' : url_prefix + 'adult.names'
}

data_dir = this_dir + '/data'

local_files = {
        'data' : data_dir + '/adult.data',
        'test' : data_dir + '/adult.test',
        'info' : data_dir + '/adult.names'
}

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

print("Moving though required files...")

for key, value in local_files.items():
    file_name = value
    if not os.path.isfile(file_name):
        url = remote_files[key]
        urllib.request.urlretrieve(url, file_name)

print("All preparations are done")