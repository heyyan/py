import json

with open('PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\coffee_sales.json', 'r') as f:
    data = json.load(f)

print(type(data))

json_string = json.dumps(data)
print(type(json_string))

new_data = json.loads(json_string)
print(type(new_data))

sales_data = data['sales']
locations = [location['name'] for location in data['locations']]
dates = [sale['date'] for sale in sales_data]
sales = [sale['sales'] for sale in sales_data]

coffee_data = {
    'locations': locations,
    'dates': dates,
    'sales': sales
}

for key, value in coffee_data.items():
    print(f"{key}: {value}")