import json
import os

def save_to_json(data, filename='data.json', path='.'):
    if filename[-4:] != 'json':
        filename += '.json'
    result_path=path
    with open(f'{result_path}/{filename}', 'w', encoding='utf-8') as fw:
        json.dump(data, fw, indent=4, ensure_ascii=False)

#합칠 json 파일 열기
json_path='./json_files'
files=os.listdir(json_path)
print(files)

outputs=[]
for file in files:
    json_file_path = os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    for i in range(len(json_file)):
        outputs.append(json_file[i])

output_dir='./json_results'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

save_to_json(outputs, 'train_data', output_dir) #file 이름 설정하기

print(len(outputs))