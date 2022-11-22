import json

import requests

response = requests.get("https://randomuser.me/api/")

request = response.request
print('урл запроса = ' + request.url)
print('path_url = ' + request.path_url)
print('метод запроса : ' + request.method)
print('хэдеры : '); print(request.headers)
print('тело запроса: '); print(request.body)

print('статус ответа:'); print(response.status_code)
print('хэдеры ответа:'); print(response.headers)
print('тело ответа: ')
b = json.loads(response.text)
print(json.dumps(b, indent=4))
