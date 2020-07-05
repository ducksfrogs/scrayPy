import requests

url = 'http://www.webscrapingfordatascience.com/redirlogin/'

r = requests.post(url, data={'username': 'dummy', 'password': '1234'}, allow_redirects=False)

print(r.cookies)
