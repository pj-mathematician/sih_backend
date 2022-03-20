from flask import Flask, g, request, jsonify
import sqlite3
from cryptography.fernet import Fernet

KEY = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM=".encode()
IMAGE_DATA = {
    'category_1': {
        "sub_category_1": {
            "i1": "https://cdn.discordapp.com/attachments/751667312825729074/954705082824421376/unknown.png",
            "i2": "https://cdn.discordapp.com/attachments/751667312825729074/954705146028380170/unknown.png",
            "i3": "https://cdn.discordapp.com/attachments/751667312825729074/954705201724530698/unknown.png",
            "i4": "https://cdn.discordapp.com/attachments/751667312825729074/954705249212461096/unknown.png",
            "i5": "https://cdn.discordapp.com/attachments/751667312825729074/954705290954158120/unknown.png",
            "i6": "https://cdn.discordapp.com/attachments/751667312825729074/954705365608579112/unknown.png",
            "i7": "https://cdn.discordapp.com/attachments/751667312825729074/954705431643684925/unknown.png",
            "i8": "https://cdn.discordapp.com/attachments/751667312825729074/954705476656980018/unknown.png",
            "i9": "https://cdn.discordapp.com/attachments/751667312825729074/954703845907378176/unknown.png",
        },
        "sub_category_2": {
            "i1": "https://cdn.discordapp.com/attachments/751667312825729074/954705082824421376/unknown.png",
            "i2": "https://cdn.discordapp.com/attachments/751667312825729074/954705146028380170/unknown.png",
            "i3": "https://cdn.discordapp.com/attachments/751667312825729074/954705201724530698/unknown.png",
            "i4": "https://cdn.discordapp.com/attachments/751667312825729074/954705249212461096/unknown.png",
            "i5": "https://cdn.discordapp.com/attachments/751667312825729074/954705290954158120/unknown.png",
            "i6": "https://cdn.discordapp.com/attachments/751667312825729074/954705365608579112/unknown.png",
            "i7": "https://cdn.discordapp.com/attachments/751667312825729074/954705431643684925/unknown.png",
            "i8": "https://cdn.discordapp.com/attachments/751667312825729074/954705476656980018/unknown.png",
            "i9": "https://cdn.discordapp.com/attachments/751667312825729074/954703845907378176/unknown.png",
        }
    },
    'category_2': {
        "sub_category_1": {
            "i1": "https://cdn.discordapp.com/attachments/751667312825729074/954705082824421376/unknown.png",
            "i2": "https://cdn.discordapp.com/attachments/751667312825729074/954705146028380170/unknown.png",
            "i3": "https://cdn.discordapp.com/attachments/751667312825729074/954705201724530698/unknown.png",
            "i4": "https://cdn.discordapp.com/attachments/751667312825729074/954705249212461096/unknown.png",
            "i5": "https://cdn.discordapp.com/attachments/751667312825729074/954705290954158120/unknown.png",
            "i6": "https://cdn.discordapp.com/attachments/751667312825729074/954705365608579112/unknown.png",
            "i7": "https://cdn.discordapp.com/attachments/751667312825729074/954705431643684925/unknown.png",
            "i8": "https://cdn.discordapp.com/attachments/751667312825729074/954705476656980018/unknown.png",
            "i9": "https://cdn.discordapp.com/attachments/751667312825729074/954703845907378176/unknown.png",
        },
        "sub_category_2": {
            "i1": "https://cdn.discordapp.com/attachments/751667312825729074/954705082824421376/unknown.png",
            "i2": "https://cdn.discordapp.com/attachments/751667312825729074/954705146028380170/unknown.png",
            "i3": "https://cdn.discordapp.com/attachments/751667312825729074/954705201724530698/unknown.png",
            "i4": "https://cdn.discordapp.com/attachments/751667312825729074/954705249212461096/unknown.png",
            "i5": "https://cdn.discordapp.com/attachments/751667312825729074/954705290954158120/unknown.png",
            "i6": "https://cdn.discordapp.com/attachments/751667312825729074/954705365608579112/unknown.png",
            "i7": "https://cdn.discordapp.com/attachments/751667312825729074/954705431643684925/unknown.png",
            "i8": "https://cdn.discordapp.com/attachments/751667312825729074/954705476656980018/unknown.png",
            "i9": "https://cdn.discordapp.com/attachments/751667312825729074/954703845907378176/unknown.png",
        }
    }
}

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
        f = Fernet(KEY)
        # password = f.encrypt(password.encode()).decode()
        # check if username already exists
        db = get_db()
        # check if user table exists, else create it
        cur = db.execute('select * from sqlite_master where type = "table" and name = "users"')
        user_table = cur.fetchone()
        if user_table is None:
            db.execute('create table users (username text, password text)')
        cur = db.execute('select * from users where username = ?', [username])
        user = cur.fetchone()
        if user is None:
            db.execute('insert into users (username, password) values (?, ?)', [username, password])
            db.commit()
            output = {'message': 'User created successfully.'}
            response = 200
        else:
            output = {'message': 'Username already exists.'}
            response = 401
        response = 200
        return jsonify(output), response
    else:
        output = {'message': 'Request must be JSON.'}
        response = 400
        return jsonify(output), response


@app.post('/login')
def login():
    if request.is_json:
        data = request.get_json()
        username = data['username']
        password = data['password']
        f = Fernet(KEY)
        # password = f.encrypt(password.encode()).decode()
        db = get_db()
        cur = db.execute('select * from sqlite_master where type = "table" and name = "users"')
        user_table = cur.fetchone()
        if user_table is None:
            db.execute('create table users (username text, password text)')
        cur = db.execute('select * from users where username = ? and password = ?', [username, password])
        user = cur.fetchone()
        if user is None:
            output = {'message': 'Invalid username or password.'}
            response = 401
        else:
            output = {'message': 'User logged in successfully.'}
            response = 200
        return jsonify(output), response
    else:
        output = {'message': 'Request must be JSON.'}
        response = 400
        return jsonify(output), response


@app.get('/images/<category>/<sub_category>')
def get_images(category, sub_category):
    if category in IMAGE_DATA and sub_category in IMAGE_DATA[category]:
        output = IMAGE_DATA[category][sub_category]
        response = 200
    else:
        output = {'message': 'Category or sub_category does not exist.'}
        response = 400
    return jsonify(output), response

@app.get('/alluserdata')
def get_all_user_data():
    db = get_db()
    cur = db.execute('select * from sqlite_master where type = "table" and name = "users"')
    user_table = cur.fetchone()
    if user_table is None:
        db.execute('create table users (username text, password text)')
    cur = db.execute('select * from users')
    users = cur.fetchall()
    output = {'users': users}
    response = 200
    return jsonify(output), response

if __name__ == '__main__':
    app.run()
