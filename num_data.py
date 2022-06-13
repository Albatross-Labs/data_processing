import json
import os

json_path='./json_results'
files=os.listdir(json_path)

for file in files:
    json_file_path = os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    print(f'{file}: {len(json_file)}')