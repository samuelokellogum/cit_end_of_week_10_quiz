from flask import Flask
from urllib.request import urlopen
import requests

app = Flask(__name__)
url = "https://www.cbsnews.com/latest/rss/main"
page = requests.get(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)
