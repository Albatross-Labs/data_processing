import json
import random

'''

'''

def train_dev_test_split(list):
    train_num = int(len(list) / 10 * 8) #train 80%
    dev_num = int(len(list) / 10 * 1) #dev 10%
    #test_num = int(len(json_file) / 10 * 1) #test는 dev 이후부터 마지막까지 포함하면 10%

    print(train_num)
    print(dev_num)

    train_list=list[:train_num+1]
    dev_list=list[train_num+1:train_num+dev_num+1]
    test_list=list[train_num+dev_num+1:]

    ### 겹치는 데이터 있는지 확인하기
    print(train_list[-1])
    print(dev_list[0])
    print(dev_list[-1])
    print(test_list[0])

    ### train, dev, test 데이터 개수 확인하기
    print(f'train data 개수: {len(train_list)}')
    print(f'dev data 개수: {len(dev_list)}')
    print(f'test data 개수: {len(test_list)}')
    print(f'전체 data 개수: {len(train_list)+len(dev_list)+len(test_list)}')

    return train_list, dev_list, test_list

def save_json(train_json, dev_json, test_json, path='./results'):

    ###train_json 저장하기
    filename='second_stove_train_data.json' #파일명 설정
    with open(f'{path}/{filename}', 'w', encoding='utf-8') as fw:
        json.dump(train_json, fw, indent=4, ensure_ascii=False)

    ###dev_json 저장하기
    filename='second_stove_dev_data.json' #파일명 설정
    with open(f'{path}/{filename}', 'w', encoding='utf-8') as fw:
        json.dump(dev_json, fw, indent=4, ensure_ascii=False)

    ###train_json 저장하기
    filename='second_stove_test_data.json' #파일명 설정
    with open(f'{path}/{filename}', 'w', encoding='utf-8') as fw:
        json.dump(test_json, fw, indent=4, ensure_ascii=False)



json_file_path='./results/second_data.json'
with open(json_file_path, 'r', encoding='utf-8') as f:
    json_file=json.load(f)

print(len(json_file)) #총 데이터 개수 확인

random.shuffle(json_file) #랜덤하게 섞기

train_json, dev_json, test_json=train_dev_test_split(json_file)
save_json(train_json, dev_json, test_json)


