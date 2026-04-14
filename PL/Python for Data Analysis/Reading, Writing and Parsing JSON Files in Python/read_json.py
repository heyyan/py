import json

with open('PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\coffee_sales_1.json', 'r') as file:
    data = json.load(file)


for item in data:
    print(item)
