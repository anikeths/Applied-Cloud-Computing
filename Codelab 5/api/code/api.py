from flask import Flask,render_template,jsonify,request
import json
import random
import os
import psycopg2  #to establish connection with the postgres db

app = Flask(__name__)

#establishing the connection
conn = psycopg2.connect( 
    database = os.environ.get('POSTGRES_DB'),     #"db"
    user = os.environ.get('POSTGRES_USER'),    #"postgres",
    password = os.environ.get('POSTGRES_PASSWORD'), #"postgres"
    host = os.environ.get('DB_HOST'), #"db",
    port = os.environ.get('DB_PORT')  #"5432"
    )
#Executing an MYSQL function using the execute() method
@app.route('/api/week5-random/',methods=[ 'GET'])
def week5():
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    select_stmt = "SELECT foodname, price FROM food ORDER BY random() LIMIT 1"

    cursor.execute(select_stmt)
    while True:
        try:
            cursor.execute(select_stmt)
            break

        except Exception as e:
            print(e.message)
    """

        conn = psycopg2.connect( 
    database = os.environ.get('POSTGRES_DB'), 
    user = os.environ.get('POSTGRES_USER'),
    password = os.environ.get('POSTGRES_PASSWORD'),
    host = os.environ.get('DB_HOST'),
    port = os.environ.get('DB_PORT')
    )"""
    res =list(cursor.fetchone())
    #cursor.close()
    # conn.close()
#     return jsonify({"We recommend": res[0],"price": res[1]})
    return jsonify({res[0]:res[1]})
        
@app.route('/')
def landingpage():
    return render_template('index.html')

@app.route("/api/complete-menu",methods = ['GET'])
def complete_menu():
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    select_stmt = "SELECT * FROM food"
    cursor.execute(select_stmt)
    #cursor.close()
    # conn.close()
    return jsonify(cursor.fetchall())

    

# @app.route('/api/addmeal',methods=['POST'])
# def addMeal():
#     newMeal = {'meal':request.json['meal']}
#     food.append(newMeal)
#     return jsonify({'food': food })
       
if __name__ == "__main__":
    #  app.run('0.0.0.0', port=5000,debug=True)
    port=os.environ.get('API_PORT')
    app.run('0.0.0.0',port=port,debug=True)
