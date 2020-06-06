import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/w/index.php' + \
    '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

first_h1 = html_soup.find('h1')
print(first_h1.name)
