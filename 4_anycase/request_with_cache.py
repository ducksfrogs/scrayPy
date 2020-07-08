import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

session = requests.Session()
cahed_session = CacheControl(session, cache=FileCache('.webcahe'))

response = cahed_session.get('https://docs.python.org/3/')
print(f'from_cache: {response.from_cache}')
print(f'status_code: { response.status_code }')
print(response.text)
