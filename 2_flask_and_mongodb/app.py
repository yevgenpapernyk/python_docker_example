import os

from flask import Flask
from pymongo import MongoClient


MONGO_URI = os.getenv('MONGO_URI')

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client['pugn']
collection = db['test']


@app.route('/')
def hello_world():
    count = collection.count_documents({})
    return f'<html><body>' \
           f'<h1>Hello, Docker!</h1>' \
           f'<p>We have {count} documents in the collection.</p>' \
           f'</body></html>'

