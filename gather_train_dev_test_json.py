import json
import os

def save_to_json(data, filename='data.json', path='.'):
    if filename[-4:] != 'json':
        filename += '.json'
    result_path=path
    with open(f'{result_path}/{filename}', 'w', encoding='utf-8') as fw:
        json.dump(data, fw, indent=4, ensure_ascii=False)

def gather_json (files, mode=''):
    outputs = []
    for file in files:
        if not mode in file:
            continue
        json_file_path = os.path.join(json_path, file)
        print(mode+' '+json_file_path)
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_file = json.load(f)

        for i in range(len(json_file)):
            outputs.append(json_file[i])

    output_dir = './json_results'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    save_to_json(outputs, f'final1_{mode}_data', output_dir)  # file 이름 설정하기

    print(f'{mode}: {len(outputs)}')

#json 파일과 text 파일 열기
json_path='./results'
files=os.listdir(json_path)
gather_json(files, mode='train')
gather_json(files, mode='dev')
gather_json(files, mode='test')