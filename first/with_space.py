
import requests

url = 'http://www.webscrapingfordatascience.com/pramhttp/?query=a query with spaces'
r = requests.get(url)
print(r.request.url)

print(r.text)
