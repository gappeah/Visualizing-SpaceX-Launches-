from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def fetch_spacex_lauches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return[]
    
lauches = fetch_spacex_lauches
print(lauches[0])



if __name__ == '__main__':
    app.run(debug=True)