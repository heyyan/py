import requests

# r = requests.get('https://api.github.com')
# r.status_code
# r.text
# print(r.text)

import codecs   
url = 'https://data.openei.org/files/5650/iou_zipcodes_2020.csv'
response = requests.get(url)
print(response)
text = response.iter_lines()
csv_reader= csv
print(list(response.iter_lines())[:5]) # print the first 5 lines of the response text
# r = requests.get('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')