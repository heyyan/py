import os
import json

dir = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales'
cdata = []
for filename in os.listdir(dir):
    if filename.endswith('.json'):
        with open(os.path.join(dir, filename), 'r') as file:
            data = json.load(file)
            cdata.extend(data)

for item in cdata:
    print(item)

outputfile = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\combined_coffee_sales.json'
with open(outputfile, 'w') as file:
    json.dump(cdata, file, indent=4)    