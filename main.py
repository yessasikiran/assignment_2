import configparser
import file_reader

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')
source_filename = config['source']['src']

# Read source file
source_content = file_reader.read_file(source_filename)
destination_filename = config['destination']['dest']

# Parse source content
lines = source_content.splitlines()
keys = lines[0].split(',')
values = lines[1].split(',')

# Write to destination file
with open(destination_filename, 'w') as f:
    f.write(','.join(keys) + '\n')
    f.write(','.join(values) + '\n')
    