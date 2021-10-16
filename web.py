import os.path
from datetime import datetime

from flask import Flask, render_template, request, send_file, send_from_directory, jsonify
from werkzeug.utils import secure_filename, redirect

import dhe
import he
import eff

UPLOAD_FOLDER = 'static/uploads'
filenameG = ""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = 'static/uploads'
app.config['DOWNLOAD_PATH'] = 'outputs'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        f = request.files['file']
        global filenameG
        filenameG = secure_filename(f.filename)
        systemPath = os.getcwd()  # OS Dir Path - Change this for Hosting
        f.save(systemPath + app.config['UPLOAD_FOLDER'] + '/' + filenameG)
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html')


def analyseDHE():
    dhe.analyse(filenameG)


# @app.route('/uploader', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         global filename
#         filename = secure_filename(f.filename)
#         systemPath = os.getcwd()  # OS Dir Path - Change this for Hosting
#         f.save(systemPath + app.config['UPLOAD_FOLDER'] + '/' + filename)
#         return redirect(request.referrer)


@app.route('/dhe')
def analyseDHE():
    dhe.analyse(filenameG)
    return "nothing"


@app.route('/he')
def analyseHE():
    he.analyse(filenameG)
    return "nothing"


@app.route('/eff')
def analyseYING():
    eff.analyse(filenameG)
    return "nothing"


# @app.route('/download')
# def downloadImg():
#     path = 'outputs/' + filenameG
#     return send_file(path, as_attachment=True)


# @app.route('/uploads')
# def upload():
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)

# systemPath = os.getcwd()  # OS Dir Path - Change this for Hosting
#         f.save(systemPath + app.config['UPLOAD_FOLDER'] + '/' + filename)

@app.route("/upload", methods=["POST", "GET"])
def upload():
    file = request.files['uploadFile']
    filename = secure_filename(file.filename)
    if file and allowed_file(file.filename):
        systemPath = os.getcwd()
        file.save(systemPath + '/' + app.config['UPLOAD_FOLDER'] + '/' + filename)
        filenameImage = file.filename

        today = datetime.today()
        # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        # cur.execute("INSERT INTO uploads (file_name,upload_time) VALUES (%s,%s)", [filenameImage, today])
        # conn.commit()
        # cur.close()
        msg = 'File successfully uploaded ' + file.filename + ' to the database!'
    else:
        msg = 'Invalid Upload only png, jpg, jpeg, gif'
    return jsonify({'htmlresponse': render_template('response.html', msg=msg, filenameImage=filenameImage)})


@app.route('/download')
def download():
    return send_from_directory(app.config['DOWNLOAD_PATH'], filenameG)


if __name__ == '__main__':
    app.run()
