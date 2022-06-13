import json
import os

json_path='./json_results' #final1데이터가 있는 곳
files=os.listdir(json_path)

for file in files: #train, dev, test 파일을 불러와서
    json_file_path = os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    new_json_file_path='' #새로운 json 파일 합친 거 여기에 넣기!!
    with open(new_json_file_path, 'r', encoding='utf-8') as f2:
        new_json_file = json.load(f)

    count=0
    outputs=[]
    for data in json_file: #무식한 방법으로 서치..해서..고치기...
        for new_data in new_json_file:
            if data['created']+data['user']==new_data['created']+new_data['user']:
                data['sentiment']=new_data['sentiment']
                count+=1
                outputs.append(data)

    output_dir='./final2_results'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(f'{output_dir}/final2_{file[7:]}.json', 'w', encoding='utf-8') as fw: #final2 data로 저장하기
        json.dump(outputs, fw, indent=4, ensure_ascii=False)




