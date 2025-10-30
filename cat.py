import sys

file_to_read = sys.argv[1]

with open(file_to_read, 'r') as f:
    print(f.read())