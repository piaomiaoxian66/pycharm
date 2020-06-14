import requests


url = 'https://reqres.in/api/users?page=1';

req = requests.get(url=url)
print(req.json())