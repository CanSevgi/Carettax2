from lxml import html
import requests

page = requests.get('http://169.254.34.191:5000/')
tree = html.fromstring(page.content)

print(tree)