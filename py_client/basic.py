import requests

endpoint = 'https://httpbin.org/status/200'
endpoint ='https://httpbin.org'

get_resonse = requests.get(endpoint)
print(get_resonse.text) 