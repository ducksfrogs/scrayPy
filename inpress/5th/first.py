import requests
from bs4 import BeautifulSoup


url = 'http://www.webscrapingfordatascience.com/simplejavascript/'
r = requests.get(url)

html_soup = BeautifulSoup(r.text, 'html.parser')

ul_tag = html_soup.find('ul')
print(ul_tag)

script_tag = html_soup.find('script', attrs={'src': None})
print(script_tag)
