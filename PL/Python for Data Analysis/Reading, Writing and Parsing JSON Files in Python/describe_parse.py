import json
import os
json_path = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales'

for filename in os.listdir(json_path):
    if filename.endswith('.json'):
        with open(os.path.join(json_path, filename), 'r') as file:
            data = json.load(file)
            print(f"File: {filename}:")
            print('Type:',type(data))

            if isinstance(data, list):
                print('List Items')
                for item in data:
                    print(item) 
            elif isinstance(data, dict):
                print('Dictionary Items')
                for key, value in data.items():
                    print(f"{key}: {value}")  
            else:
                print('Unknown data structure')
                print(data)
            print('-' * 60)     