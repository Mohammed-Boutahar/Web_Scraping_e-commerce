import json

with open('data.json', 'r') as file:
    data = json.load(file)
    result = data['feedback']

with open('output_cleaned.json', 'w') as file:
    json.dump(result, file)