import sys
import requests

url = sys.argv[1]
r = requests.get(url)
print('encording: (r.encording)', file=sys.stderr)
print(r.text)
