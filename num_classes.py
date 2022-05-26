import json
import os

json_path='./json_results' #train, dev, test json 파일
files=os.listdir(json_path)

sentiment_classes={}
theme_classes={}
da_classes={}

for file in files:
    json_file_path = os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    for data in json_file:
        if not data["sentiment"] in sentiment_classes.keys():
            sentiment_classes[data["sentiment"]]=1
        sentiment_classes[data["sentiment"]]+=1

        if not data["theme1"] in theme_classes.keys():
            theme_classes[data["theme1"]]=1
        theme_classes[data["theme1"]]+=1

        if not data["da"] in da_classes.keys():
            da_classes[data["da"]]=1
        da_classes[data["da"]]+=1

    print(f'{file}, {len(file)}, {sentiment_classes} \n {theme_classes} \n {da_classes}')