import requests
from bs4 import BeautifulSoup
from flask import Flask
import os
from lxml import etree
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class CbsNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    link = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
 

    @app.route('/')
    def index():
        url = "https://www.cbsnews.com/latest/rss/main"
        page = requests.get(url)
        data = page.json()
        # html_path = os.path.join(os.path.dirname(__file__), url) 
        # root = etree.fromstring(url)
        
        return page
        # result = etree.tostring(root)   
        # with open(result, 'r') as html_file:
        #    doc = html_file.read()

        # soup = BeautifulSoup(doc, 'html.parser')
        # return soup


    @app.route('/cbs_news')
    def cbs_news():
        pass

if __name__ == "__main__":
    index()
    app.run(debug =True)