import requests

# endpoint = 'https://httpbin.org/status/200'
endpoint ='http://127.0.0.1:8000/api/products/'

data={
    'title':'hello world',
    'price':32.00}
get_resonse = requests.post(endpoint,json=data)
print(get_resonse.status_code) 
print(get_resonse.json()) 
