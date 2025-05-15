import requests

# endpoint = 'https://httpbin.org/status/200'
endpoint ='http://127.0.0.1:8000/api/products/1/update/'

get_resonse = requests.put(endpoint, json={'title':'hello world updated'})
print(get_resonse.status_code) 
print(get_resonse.json()) 
