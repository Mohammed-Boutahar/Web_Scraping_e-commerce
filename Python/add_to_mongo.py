import pymongo
import json
import pandas as pd
import os
from pymongo import MongoClient

# connect to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["data_aliexpress"]
coll = db["collection_aliexp"]

product_keys_list = []
# Get the list of files in the current directory
files = os.listdir(".")
# Print the name of each file
for file in files:
    # Check if the file name starts with "data_"
    if file.startswith("data_"):
        # If it does, print the file name
        product_keys_list.append(file)

coll.delete_many({})

# insert documents from json files into mongodb
for i in product_keys_list:
    #    file_path = 'Python/'
    #    file_full_path = os.path.join(file_path, i)
    with open(i, 'r', encoding='utf-8') as file:
        data_str = json.load(file)


    data_s = data_str['feedback']
    print(data_s)
    # prob dans le chunk_size, il vaire selon le json

    for obj in data_s:
        new_obj = {
            'displayName': obj['displayName'],
            'country': obj['country'],
            'rating': obj['rating'],
            'date': obj['date'],
            'content': obj['content']
        }

        # Insert the new object into the MongoDB collection
        coll.insert_one(new_obj)


# export data from mongodb to a csv file
dataout = pd.DataFrame(list(coll.find()))
dataout.to_csv('../final_scraped_data.csv', encoding='utf-8')
