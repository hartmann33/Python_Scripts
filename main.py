import requests
from datetime import datetime

print(datetime.now())

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

print(datetime.now())
