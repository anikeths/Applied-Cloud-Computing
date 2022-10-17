from flask import Flask,render_template,jsonify
import json
import random

app = Flask(__name__)
 
food = {"Pizza" : 5, "Chocolate": 4, "Dosa" : 1, "croissant":2,"Amortentia":20 , "Polyjuice":12 , "Felix Felicis":43 , "Skele-Gro": 22,
"Wolfsbane":12, "Veritaserum":14 , "Jawbind": 20 , "Quodpot" : 25, "Wonton" :23, "Mocha" : 16, "Machiato" : 18 }

#on invoking localhost:5000, we get the rendering of 'index.html' file
@app.route('/')
def landingpage():
    return render_template('index.html')

#displays the complete food dictionary  localhost:5000/api/food/
@app.route("/api/food",methods = ['GET'])
def food_dictionary():
    return jsonify({"food":food})
  
#displays the random food pick on localhost:5000/api/random/
@app.route('/api/random',methods= ['GET'])
def randres():
     res = key, val = random.choice(list(food.items()))
     return jsonify({"Food: ": key, "Price ($): ": val})
#      key1 = random.choice(list(food))
#      return str(key1) + ':' + str(food[key1])

if __name__ == "__main__":
#      app.run('0.0.0.0', port=5000,debug=True)
     #to avoid hard-coded dependency
     port= os.environ.get('API_PORT')
     app.run('0.0.0.0', port=port,debug=True)
    
