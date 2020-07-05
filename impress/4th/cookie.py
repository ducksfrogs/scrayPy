import requests

url = 'http://www.webscrapingfordatascience.com/cookielogin/'

r = requests.post(url, data={'username': 'dummy', 'password': '1234'})
my_cookies = r.cookies

my_cookies['PHPSESSID'] = r.cookies.get('PHPSESSID')

r = requests.get(url + 'secret.php', cookies=my_cookies)

print(r.text)
