from flask import Flask, g, request, jsonify
import sqlite3

DATABASE = './database.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.post('/signup')
def signup():
    if request.is_json:
        data = request.get_json()
        username = data['username']
        password = data['password']
        db = get_db()
        db.execute('insert into users (username, password) values (?, ?)', [username, password])
        db.commit()
        return 'User created successfully'
    else:
        return 'Bad request'
    # return 'Signup'

if __name__ == '__main__':
    app.run()
