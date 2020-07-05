import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://python.org/robots.txt')
rp.read()
