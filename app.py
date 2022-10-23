import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
url = "https://www.cbsnews.com/latest/rss/main"
page = requests.get(url)

print(page)
