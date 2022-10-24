import os
import json
import requests
from lxml import etree
from flask import Flask, render_template
from datetime import datetime
from bs4 import BeautifulSoup
from models import model

app = Flask(__name__)

@app.route('/cbs_news', methods=["GET"])
def cbs_news():
    url = "https://www.cbsnews.com/latest/rss/main"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="xml")
    
    # return soup.find_all('item')
    my_list = {}
    for data in soup:
        val = {
            "title": data.title.text,
            "link": data.link.text,
            "description": data.description.text,
            "image": data.image.text,
        }
        
        my_list['data'] = val 
    return my_list

if __name__ == "__main__":
    index()
    app.run(debug =True)