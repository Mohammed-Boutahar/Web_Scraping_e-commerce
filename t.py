import pymongo
import json
import pandas as pd
import numpy as np
import jsonlines
from pymongo import MongoClient

#connect to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["data_ali_phone"]
coll = db["collection_phone"]

#coll.insert_many(data)
coll.delete_many({})

#insert documents from json filles into mongodb
for i in range(1,3):
    filename = f"data{i}.json"
    with open(filename,'r') as fille:
        data = json.load(fille)

    #split the data into chunks and insert into mongodb
    chunk_size = 1000
    chunks = np.array_split(data, len(data) // chunk_size + 1)
    print(chunks)
    for chunk in chunks:
        documents = []
        for item in chunk:
            doc = {
                #'name': item['name'],
                'displayName': item['displayName'],
                'country': item['country'],
                'rating': item['rating'],
                #'info': item['info'],
                'date': item['date'],
                'content': item['content'],
                #'photos': item['photos'],
            }
            documents.append(doc)
        coll.insert_many(documents)

#export data from mongodb to a csv fille
dataout = pd.DataFrame(list(coll.find()))
dataout.to_csv('phone.csv', encoding='utf-8')