from flask import Flask, g, request, jsonify
from flask_cors import CORS
import sqlite3
from cryptography.fernet import Fernet

KEY = "TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM=".encode()

IMAGE_DATA_2 = {
    "cat_1":{
        "name":"category_1",
        "address":"cat_1",
        "children": {
            "cat_1_1": {
                "name": "sub_category_1",
                "address": "cat_1/cat_1_1",
                "children": None
            },
            "cat_1_2": {
                "name": "sub_category_2",
                "address": "cat_1/cat_1_2",
                "children": None
            }
        }
    },
    "cat_2":{
        "name":"category_2",
        "address":"cat_2",
        "children": {
            "cat_2_1": {
                "name": "sub_category_1",
                "address": "cat_2/cat_2_1",
                "children": None
            },
            "cat_2_2": {
                "name": "sub_category_2",
                "address": "cat_2/cat_2_2",
                "children": None
            }
        }
    }
}


IMAGE_DATA = {"Cars": {"sedans": {"image_0": "https://i.imgur.com/JgxpyZO.jpg", "image_1": "https://i.imgur.com/JgxpyZO.jpg", "image_2": "https://i.imgur.com/ecMop22.jpg", "image_3": "https://i.imgur.com/JgxpyZO.jpg", "image_4": "https://i.imgur.com/ecMop22.jpg", "image_5": "https://i.imgur.com/XY0lnP6.jpg", "image_6": "https://i.imgur.com/JgxpyZO.jpg", "image_7": "https://i.imgur.com/ecMop22.jpg", "image_8": "https://i.imgur.com/XY0lnP6.jpg", "image_9": "https://i.imgur.com/BTacI41.jpg", "image_10": "https://i.imgur.com/JgxpyZO.jpg", "image_11": "https://i.imgur.com/ecMop22.jpg", "image_12": "https://i.imgur.com/XY0lnP6.jpg", "image_13": "https://i.imgur.com/BTacI41.jpg", "image_14": "https://i.imgur.com/NdowwBe.jpg", "image_15": "https://i.imgur.com/JgxpyZO.jpg", "image_16": "https://i.imgur.com/ecMop22.jpg", "image_17": "https://i.imgur.com/XY0lnP6.jpg", "image_18": "https://i.imgur.com/BTacI41.jpg", "image_19": "https://i.imgur.com/NdowwBe.jpg", "image_20": "https://i.imgur.com/LyLXYk8.jpg", "image_21": "https://i.imgur.com/JgxpyZO.jpg", "image_22": "https://i.imgur.com/ecMop22.jpg", "image_23": "https://i.imgur.com/XY0lnP6.jpg", "image_24": "https://i.imgur.com/BTacI41.jpg", "image_25": "https://i.imgur.com/NdowwBe.jpg", "image_26": "https://i.imgur.com/LyLXYk8.jpg", "image_27": "https://i.imgur.com/3zeJAYx.jpg", "image_28": "https://i.imgur.com/JgxpyZO.jpg", "image_29": "https://i.imgur.com/ecMop22.jpg", "image_30": "https://i.imgur.com/XY0lnP6.jpg", "image_31": "https://i.imgur.com/BTacI41.jpg", "image_32": "https://i.imgur.com/NdowwBe.jpg", "image_33": "https://i.imgur.com/LyLXYk8.jpg", "image_34": "https://i.imgur.com/3zeJAYx.jpg", "image_35": "https://i.imgur.com/JdTIvXv.jpg"}, "suv": {"image_36": "https://i.imgur.com/uk9M5iO.jpg", "image_37": "https://i.imgur.com/uk9M5iO.jpg", "image_38": "https://i.imgur.com/WFI0BKM.jpg", "image_39": "https://i.imgur.com/uk9M5iO.jpg", "image_40": "https://i.imgur.com/WFI0BKM.jpg", "image_41": "https://i.imgur.com/OFapzQL.jpg", "image_42": "https://i.imgur.com/uk9M5iO.jpg", "image_43": "https://i.imgur.com/WFI0BKM.jpg", "image_44": "https://i.imgur.com/OFapzQL.jpg", "image_45": "https://i.imgur.com/jpPxZ2w.jpg", "image_46": "https://i.imgur.com/uk9M5iO.jpg", "image_47": "https://i.imgur.com/WFI0BKM.jpg", "image_48": "https://i.imgur.com/OFapzQL.jpg", "image_49": "https://i.imgur.com/jpPxZ2w.jpg", "image_50": "https://i.imgur.com/OwinWGd.jpg", "image_51": "https://i.imgur.com/uk9M5iO.jpg", "image_52": "https://i.imgur.com/WFI0BKM.jpg", "image_53": "https://i.imgur.com/OFapzQL.jpg", "image_54": "https://i.imgur.com/jpPxZ2w.jpg", "image_55": "https://i.imgur.com/OwinWGd.jpg", "image_56": "https://i.imgur.com/7vGqYQM.jpg", "image_57": "https://i.imgur.com/uk9M5iO.jpg", "image_58": "https://i.imgur.com/WFI0BKM.jpg", "image_59": "https://i.imgur.com/OFapzQL.jpg", "image_60": "https://i.imgur.com/jpPxZ2w.jpg", "image_61": "https://i.imgur.com/OwinWGd.jpg", "image_62": "https://i.imgur.com/7vGqYQM.jpg", "image_63": "https://i.imgur.com/ffIuf4L.jpg", "image_64": "https://i.imgur.com/uk9M5iO.jpg", "image_65": "https://i.imgur.com/WFI0BKM.jpg", "image_66": "https://i.imgur.com/OFapzQL.jpg", "image_67": "https://i.imgur.com/jpPxZ2w.jpg", "image_68": "https://i.imgur.com/OwinWGd.jpg", "image_69": "https://i.imgur.com/7vGqYQM.jpg", "image_70": "https://i.imgur.com/ffIuf4L.jpg", "image_71": "https://i.imgur.com/cybFvYw.jpg", "image_72": "https://i.imgur.com/uk9M5iO.jpg", "image_73": "https://i.imgur.com/WFI0BKM.jpg", "image_74": "https://i.imgur.com/OFapzQL.jpg", "image_75": "https://i.imgur.com/jpPxZ2w.jpg", "image_76": "https://i.imgur.com/OwinWGd.jpg", "image_77": "https://i.imgur.com/7vGqYQM.jpg", "image_78": "https://i.imgur.com/ffIuf4L.jpg", "image_79": "https://i.imgur.com/cybFvYw.jpg", "image_80": "https://i.imgur.com/yxv3MVI.jpg", "image_81": "https://i.imgur.com/uk9M5iO.jpg", "image_82": "https://i.imgur.com/WFI0BKM.jpg", "image_83": "https://i.imgur.com/OFapzQL.jpg", "image_84": "https://i.imgur.com/jpPxZ2w.jpg", "image_85": "https://i.imgur.com/OwinWGd.jpg", "image_86": "https://i.imgur.com/7vGqYQM.jpg", "image_87": "https://i.imgur.com/ffIuf4L.jpg", "image_88": "https://i.imgur.com/cybFvYw.jpg", "image_89": "https://i.imgur.com/yxv3MVI.jpg", "image_90": "https://i.imgur.com/xEEmrHO.jpg"}}, "Indian Food": {"main course": {"image_91": "https://i.imgur.com/gsYsb1r.jpg", "image_92": "https://i.imgur.com/gsYsb1r.jpg", "image_93": "https://i.imgur.com/TjqpzmH.jpg", "image_94": "https://i.imgur.com/gsYsb1r.jpg", "image_95": "https://i.imgur.com/TjqpzmH.jpg", "image_96": "https://i.imgur.com/ymt3feD.jpg", "image_97": "https://i.imgur.com/gsYsb1r.jpg", "image_98": "https://i.imgur.com/TjqpzmH.jpg", "image_99": "https://i.imgur.com/ymt3feD.jpg", "image_100": "https://i.imgur.com/zT11Oxc.jpg", "image_101": "https://i.imgur.com/gsYsb1r.jpg", "image_102": "https://i.imgur.com/TjqpzmH.jpg", "image_103": "https://i.imgur.com/ymt3feD.jpg", "image_104": "https://i.imgur.com/zT11Oxc.jpg", "image_105": "https://i.imgur.com/OhNOTd2.jpg", "image_106": "https://i.imgur.com/gsYsb1r.jpg", "image_107": "https://i.imgur.com/TjqpzmH.jpg", "image_108": "https://i.imgur.com/ymt3feD.jpg", "image_109": "https://i.imgur.com/zT11Oxc.jpg", "image_110": "https://i.imgur.com/OhNOTd2.jpg", "image_111": "https://i.imgur.com/C1CYP6b.jpg", "image_112": "https://i.imgur.com/gsYsb1r.jpg", "image_113": "https://i.imgur.com/TjqpzmH.jpg", "image_114": "https://i.imgur.com/ymt3feD.jpg", "image_115": "https://i.imgur.com/zT11Oxc.jpg", "image_116": "https://i.imgur.com/OhNOTd2.jpg", "image_117": "https://i.imgur.com/C1CYP6b.jpg", "image_118": "https://i.imgur.com/DqZGMip.jpg", "image_119": "https://i.imgur.com/gsYsb1r.jpg", "image_120": "https://i.imgur.com/TjqpzmH.jpg", "image_121": "https://i.imgur.com/ymt3feD.jpg", "image_122": "https://i.imgur.com/zT11Oxc.jpg", "image_123": "https://i.imgur.com/OhNOTd2.jpg", "image_124": "https://i.imgur.com/C1CYP6b.jpg", "image_125": "https://i.imgur.com/DqZGMip.jpg", "image_126": "https://i.imgur.com/yXo3lbT.jpg", "image_127": "https://i.imgur.com/gsYsb1r.jpg", "image_128": "https://i.imgur.com/TjqpzmH.jpg", "image_129": "https://i.imgur.com/ymt3feD.jpg", "image_130": "https://i.imgur.com/zT11Oxc.jpg", "image_131": "https://i.imgur.com/OhNOTd2.jpg", "image_132": "https://i.imgur.com/C1CYP6b.jpg", "image_133": "https://i.imgur.com/DqZGMip.jpg", "image_134": "https://i.imgur.com/yXo3lbT.jpg", "image_135": "https://i.imgur.com/iZN41Kj.jpg"}, "snacks": {"image_136": "https://i.imgur.com/fpj7wpm.jpg", "image_137": "https://i.imgur.com/fpj7wpm.jpg", "image_138": "https://i.imgur.com/ZMHzS6O.jpg", "image_139": "https://i.imgur.com/fpj7wpm.jpg", "image_140": "https://i.imgur.com/ZMHzS6O.jpg", "image_141": "https://i.imgur.com/bo7toVG.jpg", "image_142": "https://i.imgur.com/fpj7wpm.jpg", "image_143": "https://i.imgur.com/ZMHzS6O.jpg", "image_144": "https://i.imgur.com/bo7toVG.jpg", "image_145": "https://i.imgur.com/jj2lQjs.jpg", "image_146": "https://i.imgur.com/fpj7wpm.jpg", "image_147": "https://i.imgur.com/ZMHzS6O.jpg", "image_148": "https://i.imgur.com/bo7toVG.jpg", "image_149": "https://i.imgur.com/jj2lQjs.jpg", "image_150": "https://i.imgur.com/eryNV04.jpg", "image_151": "https://i.imgur.com/fpj7wpm.jpg", "image_152": "https://i.imgur.com/ZMHzS6O.jpg", "image_153": "https://i.imgur.com/bo7toVG.jpg", "image_154": "https://i.imgur.com/jj2lQjs.jpg", "image_155": "https://i.imgur.com/eryNV04.jpg", "image_156": "https://i.imgur.com/SoxLypk.jpg", "image_157": "https://i.imgur.com/fpj7wpm.jpg", "image_158": "https://i.imgur.com/ZMHzS6O.jpg", "image_159": "https://i.imgur.com/bo7toVG.jpg", "image_160": "https://i.imgur.com/jj2lQjs.jpg", "image_161": "https://i.imgur.com/eryNV04.jpg", "image_162": "https://i.imgur.com/SoxLypk.jpg", "image_163": "https://i.imgur.com/soDbb9c.jpg", "image_164": "https://i.imgur.com/fpj7wpm.jpg", "image_165": "https://i.imgur.com/ZMHzS6O.jpg", "image_166": "https://i.imgur.com/bo7toVG.jpg", "image_167": "https://i.imgur.com/jj2lQjs.jpg", "image_168": "https://i.imgur.com/eryNV04.jpg", "image_169": "https://i.imgur.com/SoxLypk.jpg", "image_170": "https://i.imgur.com/soDbb9c.jpg", "image_171": "https://i.imgur.com/UWWGFUP.jpg", "image_172": "https://i.imgur.com/fpj7wpm.jpg", "image_173": "https://i.imgur.com/ZMHzS6O.jpg", "image_174": "https://i.imgur.com/bo7toVG.jpg", "image_175": "https://i.imgur.com/jj2lQjs.jpg", "image_176": "https://i.imgur.com/eryNV04.jpg", "image_177": "https://i.imgur.com/SoxLypk.jpg", "image_178": "https://i.imgur.com/soDbb9c.jpg", "image_179": "https://i.imgur.com/UWWGFUP.jpg", "image_180": "https://i.imgur.com/wYfreml.jpg"}}, "Pets": {"cats": {"image_181": "https://i.imgur.com/yV5KnFO.jpg", "image_182": "https://i.imgur.com/yV5KnFO.jpg", "image_183": "https://i.imgur.com/mjLx1Pf.jpg", "image_184": "https://i.imgur.com/yV5KnFO.jpg", "image_185": "https://i.imgur.com/mjLx1Pf.jpg", "image_186": "https://i.imgur.com/wApY2sv.jpg", "image_187": "https://i.imgur.com/yV5KnFO.jpg", "image_188": "https://i.imgur.com/mjLx1Pf.jpg", "image_189": "https://i.imgur.com/wApY2sv.jpg", "image_190": "https://i.imgur.com/Ui9UeK4.jpg", "image_191": "https://i.imgur.com/yV5KnFO.jpg", "image_192": "https://i.imgur.com/mjLx1Pf.jpg", "image_193": "https://i.imgur.com/wApY2sv.jpg", "image_194": "https://i.imgur.com/Ui9UeK4.jpg", "image_195": "https://i.imgur.com/49HGho6.jpg", "image_196": "https://i.imgur.com/yV5KnFO.jpg", "image_197": "https://i.imgur.com/mjLx1Pf.jpg", "image_198": "https://i.imgur.com/wApY2sv.jpg", "image_199": "https://i.imgur.com/Ui9UeK4.jpg", "image_200": "https://i.imgur.com/49HGho6.jpg", "image_201": "https://i.imgur.com/71TyOp6.jpg", "image_202": "https://i.imgur.com/yV5KnFO.jpg", "image_203": "https://i.imgur.com/mjLx1Pf.jpg", "image_204": "https://i.imgur.com/wApY2sv.jpg", "image_205": "https://i.imgur.com/Ui9UeK4.jpg", "image_206": "https://i.imgur.com/49HGho6.jpg", "image_207": "https://i.imgur.com/71TyOp6.jpg", "image_208": "https://i.imgur.com/dvLqXfq.jpg", "image_209": "https://i.imgur.com/yV5KnFO.jpg", "image_210": "https://i.imgur.com/mjLx1Pf.jpg", "image_211": "https://i.imgur.com/wApY2sv.jpg", "image_212": "https://i.imgur.com/Ui9UeK4.jpg", "image_213": "https://i.imgur.com/49HGho6.jpg", "image_214": "https://i.imgur.com/71TyOp6.jpg", "image_215": "https://i.imgur.com/dvLqXfq.jpg", "image_216": "https://i.imgur.com/ibGnCHD.jpg", "image_217": "https://i.imgur.com/yV5KnFO.jpg", "image_218": "https://i.imgur.com/mjLx1Pf.jpg", "image_219": "https://i.imgur.com/wApY2sv.jpg", "image_220": "https://i.imgur.com/Ui9UeK4.jpg", "image_221": "https://i.imgur.com/49HGho6.jpg", "image_222": "https://i.imgur.com/71TyOp6.jpg", "image_223": "https://i.imgur.com/dvLqXfq.jpg", "image_224": "https://i.imgur.com/ibGnCHD.jpg", "image_225": "https://i.imgur.com/bIpWZwC.jpg"}, "dogs": {"image_226": "https://i.imgur.com/a1vu2c5.jpg", "image_227": "https://i.imgur.com/a1vu2c5.jpg", "image_228": "https://i.imgur.com/pVWt4ev.jpg", "image_229": "https://i.imgur.com/a1vu2c5.jpg", "image_230": "https://i.imgur.com/pVWt4ev.jpg", "image_231": "https://i.imgur.com/sOfMduJ.jpg", "image_232": "https://i.imgur.com/a1vu2c5.jpg", "image_233": "https://i.imgur.com/pVWt4ev.jpg", "image_234": "https://i.imgur.com/sOfMduJ.jpg", "image_235": "https://i.imgur.com/NICSjPH.jpg", "image_236": "https://i.imgur.com/a1vu2c5.jpg", "image_237": "https://i.imgur.com/pVWt4ev.jpg", "image_238": "https://i.imgur.com/sOfMduJ.jpg", "image_239": "https://i.imgur.com/NICSjPH.jpg", "image_240": "https://i.imgur.com/G5P6f58.jpg", "image_241": "https://i.imgur.com/a1vu2c5.jpg", "image_242": "https://i.imgur.com/pVWt4ev.jpg", "image_243": "https://i.imgur.com/sOfMduJ.jpg", "image_244": "https://i.imgur.com/NICSjPH.jpg", "image_245": "https://i.imgur.com/G5P6f58.jpg", "image_246": "https://i.imgur.com/IGUnfa1.jpg", "image_247": "https://i.imgur.com/a1vu2c5.jpg", "image_248": "https://i.imgur.com/pVWt4ev.jpg", "image_249": "https://i.imgur.com/sOfMduJ.jpg", "image_250": "https://i.imgur.com/NICSjPH.jpg", "image_251": "https://i.imgur.com/G5P6f58.jpg", "image_252": "https://i.imgur.com/IGUnfa1.jpg", "image_253": "https://i.imgur.com/t2wOpXH.jpg", "image_254": "https://i.imgur.com/a1vu2c5.jpg", "image_255": "https://i.imgur.com/pVWt4ev.jpg", "image_256": "https://i.imgur.com/sOfMduJ.jpg", "image_257": "https://i.imgur.com/NICSjPH.jpg", "image_258": "https://i.imgur.com/G5P6f58.jpg", "image_259": "https://i.imgur.com/IGUnfa1.jpg", "image_260": "https://i.imgur.com/t2wOpXH.jpg", "image_261": "https://i.imgur.com/OAXfHKz.jpg", "image_262": "https://i.imgur.com/a1vu2c5.jpg", "image_263": "https://i.imgur.com/pVWt4ev.jpg", "image_264": "https://i.imgur.com/sOfMduJ.jpg", "image_265": "https://i.imgur.com/NICSjPH.jpg", "image_266": "https://i.imgur.com/G5P6f58.jpg", "image_267": "https://i.imgur.com/IGUnfa1.jpg", "image_268": "https://i.imgur.com/t2wOpXH.jpg", "image_269": "https://i.imgur.com/OAXfHKz.jpg", "image_270": "https://i.imgur.com/jnsSlX7.jpg"}}}

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
