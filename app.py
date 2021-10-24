import os.path
from datetime import datetime

import shortuuid
from flask import Flask, render_template, request, send_file, jsonify
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import MySQLdb.cursors

import dhe
import he
import eff

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
fileAnalyse = ""
fileDownload = ""
filenameImage = ""

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mishrilal99'
app.config['MYSQL_DB'] = 'ImgEnh'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = 'static/uploads'
app.config['DOWNLOAD_PATH'] = 'static/outputs'

mysql = MySQL(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def hello_world():
    return render_template('index.html')


@app.route("/history", methods=["POST", "GET"])
def history():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM records")
    records = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    print(records)
    return render_template('records.html', records=records)


@app.route('/dhe')
def analyseDHE():
    global fileDownload
    fileDownload = dhe.analyse(fileAnalyse)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("UPDATE records SET dhe=%s WHERE upload=%s",
                (fileDownload, fileAnalyse))
    mysql.connection.commit()
    cur.close()
    return jsonify({'htmlresponse': render_template('responseOutput.html', filenameImage=fileDownload)})


@app.route('/he', methods=['GET', 'POST'])
def analyseHE():
    global fileDownload
    fileDownload = he.analyse(fileAnalyse)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("UPDATE records SET he=%s WHERE upload=%s",
                (fileDownload, fileAnalyse))
    mysql.connection.commit()
    cur.close()
    return jsonify({'htmlresponse': render_template('responseOutput.html', filenameImage=fileDownload)})


@app.route('/eff')
def analyseEFF():
    global fileDownload
    fileDownload = eff.analyse(fileAnalyse)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("UPDATE records SET eff=%s WHERE upload=%s",
                (fileDownload, fileAnalyse))
    mysql.connection.commit()
    cur.close()
    return jsonify({'htmlresponse': render_template('responseOutput.html', filenameImage=fileDownload)})


@app.route('/download')
def download():
    path = 'static/outputs/' + fileDownload
    return send_file(path, as_attachment=True)


@app.route("/upload", methods=["POST", "GET"])
def upload():
    newName = shortuuid.uuid()
    file = request.files['uploadFile']
    filename = secure_filename(file.filename)
    fileExt = filename.rsplit('.', 1)[1]
    filename = newName + '.' + fileExt
    global fileAnalyse, filenameImage
    fileAnalyse = filename
    if file and allowed_file(file.filename):
        systemPath = os.getcwd()
        file.save(systemPath + '/' + app.config['UPLOAD_FOLDER'] + '/' + filename)

        today = datetime.today()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO records(uploadTime, upload) VALUES (%s, %s)",
                    (today, filename))
        mysql.connection.commit()
        cur.close()

        msg = 'File successfully uploaded ' + file.filename + ' to the database!'
    else:
        msg = 'Invalid Upload only png, jpg, jpeg, gif'
    return jsonify({'htmlresponse': render_template('response.html', msg=msg, filenameImage=filename)})


if __name__ == '__main__':
    app.run()
