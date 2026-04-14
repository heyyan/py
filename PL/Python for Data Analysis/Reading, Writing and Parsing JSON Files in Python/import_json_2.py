import json

input_file1 = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\coffee_sales_1.json'
input_file2 = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\coffee_sales_2.json'

output_file = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\combined_coffee_sales.json'
output_file2 = 'PL\\Python for Data Analysis\\Reading, Writing and Parsing JSON Files in Python\\coffee_sales\\combined_coffee_sales2.json'

with open(input_file1, 'r') as file1, open(input_file2, 'r') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# combined_data = {
#     'locations': data1['locations'] + data2['locations'],
#     'dates': data1['dates'] + data2['dates'],
#     'sales': data1['sales'] + data2['sales']
# }

# with open(output_file, 'w') as file:
#     json.dump(combined_data, file)  


cdata = []
cdata.extend(data1)
cdata.extend(data2)

with open(output_file2, 'w') as file:
    json.dump(cdata, file)