import requests

# endpoint = 'https://httpbin.org/status/200'
product_id = input('Enter ID to delete \n')
try:
    product_id = int(product_id)
except:
    product_id = None
    print('Invalid ID')

endpoint =f'http://127.0.0.1:8000/api/products/{product_id}/delete/'

get_resonse = requests.delete(endpoint, json={'title':'hello world updated'})
print(get_resonse.status_code) 
print(get_resonse.status_code) 
