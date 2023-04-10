import os

from flask import Flask
from pymongo import MongoClient


# app
app = Flask(__name__)

# env
MONGO_URI = os.getenv('MONGO_URI')  # default: None -> then 'mongodb://localhost:27017' is used
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME', 'pugn')
MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME', 'test')

# mongo
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


@app.route('/')
def hello_world():
    count = collection.count_documents({})
    return f'<html>' \
           f'<head><title>Hello Docker</title></head>' \
           f'<body>' \
           f'<h1>Hello, Docker!</h1>' \
           f'<p>We have {count} documents in the collection "{collection.name}".</p>' \
           f'</body>' \
           f'</html>'

