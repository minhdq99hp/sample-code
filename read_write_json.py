'''
Read and Write .json file

Author: minhdq99hp
'''

import json

DATA_PATH = 'my_file.json'
# read
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# write
with open(DATA_PATH, 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=4))