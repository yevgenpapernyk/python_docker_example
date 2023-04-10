import os
from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'<html>' \
           f'<head><title>Hello Docker</title></head>' \
           f'<body>' \
           f'<h1>Hello Docker!</h1>' \
           f'<p>Date: {datetime.now()}<p>' \
           f'<p>Load: {os.getloadavg()}<p>' \
           f'</body>' \
           f'</html>'

