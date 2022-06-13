import json
import os
import matplotlib.pyplot as plt
import numpy as np

### train, dev, test json 파일에서 클래스 개수 적기

json_path='./json_results' #train, dev, test json 파일 #현재는 final1으로 되어있음
files=os.listdir(json_path)

for file in files:
    json_file_path = os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    sentiment_classes = {}
    theme_classes = {}
    da_classes = {}

    for data in json_file:
        if not data["sentiment"] in sentiment_classes.keys():
            sentiment_classes[data["sentiment"]]=1
        else:
            sentiment_classes[data["sentiment"]]+=1

        if not data["theme1"] in theme_classes.keys():
            theme_classes[data["theme1"]]=1
        else:
            theme_classes[data["theme1"]]+=1

        if not data["da"] in da_classes.keys():
            da_classes[data["da"]]=1
        else:
            da_classes[data["da"]]+=1

    print(f'{file}, {len(json_file)}, {sentiment_classes} \n {theme_classes} \n {da_classes} \n')
    print(f'sentiment sum: {sum(sentiment_classes.values())} \t theme sum: {sum(theme_classes.values())} \t da sum: {sum(da_classes.values())}\n')

'''
### 클래스 별 그래프 그리기

def draw_chart (dict, task=''):
    x=np.arange(len(dict.keys()))
    xtick=dict.keys()
    values=dict.values()

    plt.bar(x, values)
    plt.xticks(x, xtick)

    output_dir='./chart_image'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    plt.savefig(f'{output_dir}/{task}.png')

draw_chart(sentiment_classes, 'sentiment')
draw_chart(theme_classes, 'theme')
draw_chart(da_classes, 'da')

한글 폰트 깨져서 소용이 없음 어차피 엑셀로 만들어야 함...ㅎ

'''

