import os.path
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename, redirect

import dhe
import he
import eff

UPLOAD_FOLDER = '/uploads'
filename = ""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello_world():
    return render_template('index.html')


def analyseDHE():
    dhe.analyse(filename)


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        global filename
        filename = secure_filename(f.filename)
        systemPath = os.getcwd()  # OS Dir Path - Change this for Hosting
        f.save(systemPath + app.config['UPLOAD_FOLDER'] + '/' + filename)
        return redirect(request.referrer)


@app.route('/dhe', methods=['POST'])
def analyseDHE():
    dhe.analyse(filename)
    return redirect(request.referrer)


@app.route('/he', methods=['POST'])
def analyseHE():
    he.analyse(filename)
    return redirect(request.referrer)


@app.route('/eff', methods=['POST'])
def analyseYING():
    eff.analyse(filename)
    return redirect(request.referrer)


# @app.route('/dhe', methods='POST')
# def analyseDHE():
#     dhe.analyse(filename)


@app.route('/download')
def downloadImg():
    path = 'outputs/' + filename
    return send_file(path, as_attachment=True)


@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"


if __name__ == '__main__':
    app.run()
