import json
import os
import pandas as pd

csv_path='./csvfiles'
files=os.listdir(csv_path)

print(files)

results=[]

for file in files:
    csv_file_path = os.path.join(csv_path, file)
    csv_file=pd.read_csv(csv_file_path)

    print(len(csv_file))

    csv_file=csv_file.dropna(subset=['sentiment', 'theme1', 'da']) #레이블에 빈 값이 있는 행 삭제

    csv_file=csv_file.astype({'created':str, 'user':str, 'header':str, 'content':str, 'sentiment': int, 'theme1':str, 'da':str})

    print(len(csv_file)) #몇 개의 행이 남는지 확인하기

    for i in range(len(csv_file)):
        result = {}
        for column in csv_file:
            result[column]=str(csv_file.iloc[i][column])
        results.append(result)

    print(results)


with open('./results/second_data.json', 'w', encoding='utf-8') as fw:
    json.dump(results, fw, indent=4, ensure_ascii=False)
