from flask import Flask, g, request, jsonify
from flask_cors import CORS
import sqlite3
from cryptography.fernet import Fernet

KEY = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM=".encode()


IMAGE_DATA = {'cat_1': {'cat_1_1': {'image_0': 'https://i.imgur.com/mtjUCR0.jpg', 'image_1': 'https://i.imgur.com/WJN8TIE.jpg', 'image_2': 'https://i.imgur.com/WBQZNbW.jpg', 'image_3': 'https://i.imgur.com/M9vmak7.jpg', 'image_4': 'https://i.imgur.com/xrVnPCh.jpg', 'image_5': 'https://i.imgur.com/iWlVP5Z.jpg', 'image_6': 'https://i.imgur.com/t0yn2pe.jpg', 'image_7': 'https://i.imgur.com/2JHcIP7.jpg', 'image_8': 'https://i.imgur.com/rJrvjJl.jpg'}, 'cat_1_2': {'image_9': 'https://i.imgur.com/3KxMxru.jpg', 'image_10': 'https://i.imgur.com/Qsr3ayd.jpg', 'image_11': 'https://i.imgur.com/EiRTcq6.jpg', 'image_12': 'https://i.imgur.com/1aYzlzP.jpg', 'image_13': 'https://i.imgur.com/OGriEyb.jpg', 'image_14': 'https://i.imgur.com/UXK331z.jpg', 'image_15': 'https://i.imgur.com/FJTryXm.jpg', 'image_16': 'https://i.imgur.com/X2IBkla.jpg', 'image_17': 'https://i.imgur.com/UI9X1jI.jpg'}}, 'cat_2': {'cat_2_1': {'image_18': 'https://i.imgur.com/48NaaWg.jpg', 'image_19': 'https://i.imgur.com/GKhDtAM.jpg', 'image_20': 'https://i.imgur.com/eFSydhK.jpg', 'image_21': 'https://i.imgur.com/3zRlFfh.jpg', 'image_22': 'https://i.imgur.com/HaqkCAd.jpg', 'image_23': 'https://i.imgur.com/1sEwoCm.jpg', 'image_24': 'https://i.imgur.com/c5s5p9D.jpg', 'image_25': 'https://i.imgur.com/aRRfHpH.jpg', 'image_26': 'https://i.imgur.com/DxA7H1M.jpg'}, 'cat_2_2': {'image_27': 'https://i.imgur.com/Zu1SysF.jpg', 'image_28': 'https://i.imgur.com/G7GZ21K.jpg', 'image_29': 'https://i.imgur.com/QDiUvTx.jpg', 'image_30': 'https://i.imgur.com/iseK8tn.jpg', 'image_31': 'https://i.imgur.com/SeMMC5O.jpg', 'image_32': 'https://i.imgur.com/WhFEHpT.jpg', 'image_33': 'https://i.imgur.com/eLwzFN8.jpg', 'image_34': 'https://i.imgur.com/9Gw4dzh.jpg', 'image_35': 'https://i.imgur.com/8UPGW1z.jpg'}}, 'cat_3': {'cat_3_1': {'image_36': 'https://i.imgur.com/58yhtqX.jpg', 'image_37': 'https://i.imgur.com/aJPnMt0.jpg', 'image_38': 'https://i.imgur.com/gYIQcff.jpg', 'image_39': 'https://i.imgur.com/tSfbAWs.jpg', 'image_40': 'https://i.imgur.com/dqf2Vr3.jpg', 'image_41': 'https://i.imgur.com/wcK3z8Q.jpg', 'image_42': 'https://i.imgur.com/TFf8C9d.jpg', 'image_43': 'https://i.imgur.com/0WZeeSv.jpg', 'image_44': 'https://i.imgur.com/Wj0kiuc.jpg'}, 'cat_3_2': {'image_45': 'https://i.imgur.com/Ayb4Jxs.jpg', 'image_46': 'https://i.imgur.com/f00sMvW.jpg', 'image_47': 'https://i.imgur.com/t4BXxkI.jpg', 'image_48': 'https://i.imgur.com/sjzHecC.jpg', 'image_49': 'https://i.imgur.com/lVsJGFw.jpg', 'image_50': 'https://i.imgur.com/dshobzE.jpg', 'image_51': 'https://i.imgur.com/UCnYSqA.jpg', 'image_52': 'https://i.imgur.com/GYdAfNA.jpg', 'image_53': 'https://i.imgur.com/rKfyxiQ.jpg'}}}

IMAGE_DATA_2 = {
    "cat_1":{
        "name":"Cars",
        "address":"cat_1",
        "children": {
            "cat_1_1": {
                "name": "sedans",
                "address": "cat_1/cat_1_1",
                "children": None
            },
            "cat_1_2": {
                "name": "suv",
                "address": "cat_1/cat_1_2",
                "children": None
            }
        }
    },
    "cat_2":{
        "name":"Indian Food",
        "address":"cat_2",
        "children": {
            "cat_2_1": {
                "name": "main course",
                "address": "cat_2/cat_2_1",
                "children": None
            },
            "cat_2_2": {
                "name": "snacks",
                "address": "cat_2/cat_2_2",
                "children": None
            }
        }
    },
    "cat_3":{
        "name":"Pets",
        "address":"cat_3",
        "children": {
            "cat_3_1": {
                "name": "cats",
                "address": "cat_3/cat_3_1",
                "children": None
            },
            "cat_3_2": {
                "name": "dogs",
                "address": "cat_3/cat_3_2",
                "children": None
            }
        }
    }
}

DATABASE = './database.db'
app = Flask(__name__)
CORS(app)

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

@app.get('/images/<category>')
def get_image_sub_categories(category):
    if category in IMAGE_DATA:
        output = list(IMAGE_DATA[category].keys())
        response = 200
    else:
        output = {'message': 'Category does not exist.'}
        response = 400
    return jsonify(output), response

@app.get('/images')
def get_image_categories():
    output = list(IMAGE_DATA.keys())
    response = 200
    return jsonify(output), response

@app.get("/images2")
def get_images2():
    output = IMAGE_DATA_2
    response = 200
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
