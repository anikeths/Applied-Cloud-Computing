from flask import Flask,render_template,jsonify
import requests
import json
import random
import os

app = Flask(__name__)

@app.route('/api/random',methods= ['GET'])
def randres():
    res = key, val = random.choice(list(food.items()))
    return (str(res))

#communicates with the API container and writes what it is getting from api TO food.html template file and renders it.
@app.route('/',methods= ['GET'])
def index():
    res = requests.get('http://api:5000/api/random')
    food_item = res.text
    return render_template('food.html', food=food_item)

if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 3001))
    # app.run('127.0.0.1', port = port,debug=True)
    app.run(debug=True, host='0.0.0.0', port=80)
