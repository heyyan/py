import requests
import json

url = 'https://www.edfreitas.me/test/wired_brain.json'
response = requests.get(url)
if response.status_code == 200:
    # data = response.json()
    # print(data)
    date = json.loads(response.text)
    for item in date:
        print(item)
    # print(date)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")