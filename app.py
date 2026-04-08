from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Aaron in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_ezvh_user:S1wL8a2O2WBj4TsKvKdlDcTm7d6OmwO9@dpg-d7asec2li9vc73fhtatg-a/flask_hello_world_db_ezvh")
    conn.close
    return "Database Connection Successful"