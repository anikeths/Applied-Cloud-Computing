from flask import Flask,render_template,jsonify
import requests
import json
import random
import os

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def index():
    host = os.environ.get('API_HOST')
    port = os.environ.get('API_PORT')
    endpoint = os.environ.get('API_ENDPOINT')
    url = f'http://{host}:{port}/{endpoint}'
    res = requests.get(url)
#   res = requests.get('http://api:5000/api/random')
    # food_item = res.text
    return render_template('food.html', food=res)

if __name__ == "__main__":
    port=os.environ.get('CONSUMER_PORT')
    app.run(debug=True, host='0.0.0.0', port=port)
