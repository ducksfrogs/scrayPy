import requests

url = 'http://www.webscrapingfordatascience.com/pramhttp/?query=test'
r = requests.get(url)
print(r.text)
