import json
import re
from bs4 import BeautifulSoup
import os
#from soynlp.normalizer import *
#from pykospacing import Spacing

'''
화행은 문장부호는 남기는 것으로
주제는 다 지우는 것으로
감성은 반복만 줄이는 것으로 
'''

def text_normalize(text):
    # html 태그 지우기
    soup = BeautifulSoup(text, "html5lib")
    text = soup.get_text()

    text=re.sub('https://.*', ' ', text) #https://로 시작하는 주소들 지우기
    #text = re.sub('\W', ' ', text)  # 문장 부호 및 특수문자 지우기

    '''
    #의미없게 반복되는 것 삭제
    text=emoticon_normalize(text)
    text=repeat_normalize(text)
    '''

    text = re.sub('([ㄱ-ㅎㅏ-ㅣ]+)', ' ', text)  # 한글 자음, 한글 모음
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r' ', text)  # 유니코드로 이모티콘 지우기

    text = ' '.join(text.split())  # 쓸데 없이 추가된 공백 제거

    '''
    #문장 띄어쓰기 정규화
    spacing=Spacing()
    text=spacing(text)
    '''

    return text

### json 파일 열기

json_path='./normalize_files'
files=os.listdir(json_path)

for file in files:
    json_file_path=os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file=json.load(f)

    for i in range(len(json_file)):
        ### header 수정
        text_tmp = json_file[i]['header'] #text 데이터로 들어갈 부분 불러오기
        json_file[i]['header']=text_normalize(text_tmp)

        ### content 수정
        text_tmp = json_file[i]['content']  # text 데이터로 들어갈 부분 불러오기
        json_file[i]['content'] = text_normalize(text_tmp)

    #json 파일 저장
    output_dir='./normalize_results'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f'{output_dir}/normalize_da_{file}', 'w', encoding='utf-8') as fw: #sentiment인지, 화행인지, 주제인지 먼저 보기
        json.dump(json_file, fw, indent=4, ensure_ascii=False)

