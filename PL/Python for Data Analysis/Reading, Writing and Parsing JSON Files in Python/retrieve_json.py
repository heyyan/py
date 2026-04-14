import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'

headers = {
    'Content-Type': 'application/json',
}

parameters = {
    'name': 'Clementina DuBuque'
}

response = requests.get(url, headers=headers, params=parameters)
if response.status_code == 200:
    # data = response.json()
    # print(data)
    date = json.loads(response.text)
    for item in date:
        print(item)
    # print(date)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
