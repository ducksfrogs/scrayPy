import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
    '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)
html_content = r.text
html_soup = BeautifulSoup(html_content, 'html.parser')
first_h1 = html_soup.find('h1')

print(first_h1.name)
print(first_h1.contents)

print(str(first_h1))
print(first_h1.attrs['id'])
print('----CITATIONS-----')
cites = html_soup.find_all('cite', class_='citation', limit=5)

for cite in cites:
    print(cite.get_text())
    link = cite.find('a')
    print(link.get('href'))
    print()
