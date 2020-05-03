import requests
from pprint import pprint
url = 'http://localhost:8080/process'
headers = {'Content-Type': 'application/json'}
payload = {"num1": [1, 2, 3], "num2":[4, 5, 6]}
pprint(payload)
response = requests.post(url, headers=headers, data=payload)
pprint(response.json)
pprint(response.text)
pprint(response.status_code)

