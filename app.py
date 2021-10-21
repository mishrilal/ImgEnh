import os.path
import time
from datetime import datetime
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename

import dhe
import he
import eff

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'mishrilal99'
# app.config['MYSQL_DB'] = 'ImgEnh'
#
# mysql = MySQL(app)

UPLOAD_FOLDER = 'static/uploads'
fileAnalyse = ""
fileDownload = ""
filenameImage = ""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = 'static/uploads'
app.config['DOWNLOAD_PATH'] = 'static/outputs'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def hello_world():
    # if request.method == "POST":
    #     f = request.files['file']
    #     global filenameG
    #     filenameG = secure_filename(f.filename)
    #     systemPath = os.getcwd()  # OS Dir Path - Change this for Hosting
    #     f.save(systemPath + app.config['UPLOAD_FOLDER'] + '/' + filenameG)
    # files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html')


@app.route('/dhe')
def analyseDHE():
    global fileDownload
    fileDownload = dhe.analyse(fileAnalyse)
    return jsonify({'htmlresponse': render_template('responseOutput.html', filenameImage=fileDownload)})


@app.route('/he', methods=['GET', 'POST'])
def analyseHE():
    global fileDownload
    fileDownload = he.analyse(fileAnalyse)
    return jsonify({'htmlresponse': render_template('responseOutput.html', filenameImage=fileDownload)})


@app.route('/eff')
def analyseEFF():
    global fileDownload
    fileDownload = eff.analyse(fileAnalyse)
    return jsonify({'htmlresponse': render_template('responseOutput.html', filenameImage=fileDownload)})


@app.route('/download')
def download():
    path = 'static/outputs/' + fileDownload
    return send_file(path, as_attachment=True)


@app.route("/upload", methods=["POST", "GET"])
def upload():
    file = request.files['uploadFile']
    filename = secure_filename(file.filename)
    global fileAnalyse, filenameImage
    fileAnalyse = filename
    if file and allowed_file(file.filename):
        systemPath = os.getcwd()
        file.save(systemPath + '/' + app.config['UPLOAD_FOLDER'] + '/' + filename)
        filenameImage = file.filename

        # today = datetime.today()
        # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) cur.execute("INSERT INTO uploads (file_name,
        # upload_time) VALUES (%s,%s)", [filenameImage, today]) conn.commit() cur.close() cur =
        # mysql.connection.cursor() cur.execute("INSERT INTO records(date, upload) VALUES (%s, %s)", (today,
        # systemPath + '/' + app.config['UPLOAD_FOLDER'] + '/' + filename)) mysql.connection.commit() cur.close()
        msg = 'File successfully uploaded ' + file.filename + ' to the database!'
    else:
        msg = 'Invalid Upload only png, jpg, jpeg, gif'
    return jsonify({'htmlresponse': render_template('response.html', msg=msg, filenameImage=filenameImage)})


if __name__ == '__main__':
    app.run()
