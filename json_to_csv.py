import json
import os
import pandas as pd

json_path='./jsonfiles'
files=os.listdir(json_path)

data={"created":[], "user":[], "header":[], "content":[]}

for file in files:
    json_file_path = os.path.join(json_path, file)
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_file = json.load(f)

    for d in json_file:
        data["created"].append(d["created"])
        data["user"].append(str(d["user"]))
        data["header"].append(d["header"])
        data["content"].append(d["content"])

data=pd.DataFrame(data)

data.to_csv('./results/Data3000.csv', sep=',', na_rep='NaN', index=False, encoding='utf-8')
